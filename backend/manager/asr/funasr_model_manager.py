from manager.asr.interface.asr_model_manager import ASRModelManager
from model.transcription_segment import TranscriptionSegment
from torch.cuda import is_available
from typing import List
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
import soundfile as sf
import io


def load_audio_with_fallback(audio_path: str, target_sr: int = 16000):
    """加载音频，支持多种格式（包括aac），统一转换为16kHz"""
    try:
        # 尝试用 soundfile 读取
        waveform, sample_rate = sf.read(audio_path)
    except Exception:
        # 如果失败（如aac格式），使用 pydub + ffmpeg
        try:
            import pydub
            from pydub import AudioSegment

            audio = AudioSegment.from_file(audio_path)
            # 转换为目标采样率
            if audio.frame_rate != target_sr:
                audio = audio.set_frame_rate(target_sr)
            # 转换为单声道
            if audio.channels > 1:
                audio = audio.set_channels(1)
            # 导出为wav格式到内存
            buffer = io.BytesIO()
            audio.export(buffer, format="wav")
            buffer.seek(0)
            waveform, sample_rate = sf.read(buffer)
        except ImportError:
            raise ImportError("请安装 pydub: pip install pydub，并确保已安装 ffmpeg")

    # 转为单声道
    if len(waveform.shape) > 1:
        waveform = waveform.mean(axis=1)

    # 转为 float32
    if waveform.dtype != "float32":
        waveform = waveform.astype("float32")

    # 重采样到目标采样率（SenseVoice需要16kHz）
    if sample_rate != target_sr:
        try:
            import librosa

            waveform = librosa.resample(
                waveform, orig_sr=sample_rate, target_sr=target_sr
            )
            sample_rate = target_sr
        except ImportError:
            raise ImportError(
                f"音频采样率为{sample_rate}Hz，需要{target_sr}Hz，请安装 librosa: pip install librosa"
            )

    return waveform, sample_rate


class FunasrModelManager(ASRModelManager):
    def __init__(self, model_size: str, device: str | None = None) -> None:
        super().__init__()
        self.model: AutoModel | None = None
        self.model_size: str = model_size
        self.vad_model: AutoModel | None = None
        self.device: str = "cuda" if not device and is_available() else "cpu"

    def load_model(self) -> None:
        self.model = AutoModel(
            model="iic/SenseVoiceSmall", trust_remote_code=False, device="cuda:0"
        )
        self.vad_model = AutoModel(model="fsmn-vad")

    def unload_model(self) -> None:
        del self.model
        self.model: AutoModel | None = None

    def transcribe(self, audio: str) -> List[TranscriptionSegment]:
        if not self.model or not self.vad_model:
            self.load_model()
        if self.model and self.vad_model:
            # 1. VAD 检测语音段落（VAD 可以直接处理文件路径）
            vad_result = self.vad_model.generate(input=audio)
            assert type(vad_result) is list
            segments = vad_result[0]["value"]

            # 2. 读取完整音频（支持多种格式）
            waveform, sample_rate = load_audio_with_fallback(audio)

            # 3. 对每个 VAD 段落分别进行 ASR
            transcription_segments: List[TranscriptionSegment] = []
            for idx, (start_ms, end_ms) in enumerate(segments):
                # 转换为采样点索引
                start_sample = int(start_ms * sample_rate / 1000)
                end_sample = int(end_ms * sample_rate / 1000)

                # 裁剪音频段落
                segment_audio = waveform[start_sample:end_sample]

                # 对该段落进行识别
                result = self.model.generate(
                    input=segment_audio, language="auto", use_itn=False
                )
                assert type(result) is list

                # 提取并清理文本
                text = ""
                if result and len(result) > 0:
                    raw_text = result[0].get("text", "")
                    text = rich_transcription_postprocess(raw_text)

                transcription_segments.append(
                    TranscriptionSegment(
                        start=start_ms / 1000.0,  # 转换为秒
                        end=end_ms / 1000.0,
                        text=text.strip(),
                    )
                )

            return transcription_segments
        return []
