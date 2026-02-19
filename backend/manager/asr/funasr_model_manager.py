from manager.asr.interface.asr_model_manager import ASRModelManager
from model.transcription_segment import TranscriptionSegment
from torch.cuda import is_available
from typing import List, Dict
from funasr import AutoModel


class FunasrModelManager(ASRModelManager):

    def __init__(
        self,
        model_size: str,
        device: str | None = None
    ) -> None:
        super().__init__()
        self.model: AutoModel | None = None
        self.model_size: str = model_size
        self.vad_model: AutoModel | None = None
        self.device: str = 'cuda' if not device and is_available() else 'cpu'

    def load_model(self) -> None:
        self.model = AutoModel(
            model="iic/SenseVoiceSmall",
            trust_remote_code=True,
            device="cuda:0"
        )
        self.vad_model = AutoModel(model='fsmn-vad')

    def unload_model(self) -> None:
        del self.model
        self.model: AutoModel | None = None

    def transcribe(self, audio: str) -> List[TranscriptionSegment]:
        if not self.model or not self.vad_model:
            self.load_model()
        if self.model and self.vad_model:
            vad_result = self.vad_model.generate(
                input=audio
            )
            assert type(vad_result) is Dict
            # vad_result 输出示例
    #       [
    #           {
    #             "key": "speech",
    #             "value": [
    #                 [
    #                     3880,
    #                     11090
    #                 ],
            segments = vad_result[0]['value']
            for (start, end) in segments:
                assert (type(start), type(end)) is (int, int)
