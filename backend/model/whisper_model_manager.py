from model.interface.asr_model_manager import ASRModelManager
from model.transcription_segment import TranscriptionSegment
from faster_whisper import WhisperModel
from torch.cuda import is_available
from typing import List


class WhisperModelManager(ASRModelManager):

    def __init__(
        self,
        model_size: str,
        device: str | None = None
    ) -> None:
        super().__init__()
        self.model: WhisperModel | None = None
        self.model_size: str = model_size
        self.device: str = 'cuda' if not device and is_available() else 'cpu'

    def load_model(self) -> None:
        self.model = WhisperModel(
            model_size_or_path=self.model_size,
            device=self.device
        )

    def unload_model(self) -> None:
        del self.model
        self.model: WhisperModel | None = None

    def transcribe(self, audio: str) -> List[TranscriptionSegment]:
        if not self.model:
            self.load_model()
        if self.model:
            segments: List[TranscriptionSegment] = []
            (result_segments, _) = self.model.transcribe(audio=audio)
            for item in result_segments:
                segments.append(TranscriptionSegment(
                    start=round(item.start, 2),
                    end=round(item.end, 2),
                    text=item.text
                ))
            return segments
        else:
            raise TypeError("model is None")
