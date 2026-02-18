from manager.asr.interface.asr_model_manager import ASRModelManager
from model.transcription_segment import TranscriptionSegment
from torch.cuda import is_available
from typing import List
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
        self.device: str = 'cuda' if not device and is_available() else 'cpu'

    def load_model(self) -> None:
        ...

    def unload_model(self) -> None:
        ...

    def transcribe(self, audio: str) -> List[TranscriptionSegment]:
        ...
