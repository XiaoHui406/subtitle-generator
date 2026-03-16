from abc import ABC, abstractmethod
from typing import List
from model.asr.transcription_segment import TranscriptionSegment


class ASRModelManager(ABC):

    @abstractmethod
    def load_model(self) -> None:
        ...

    @abstractmethod
    def unload_model(self) -> None:
        ...

    @abstractmethod
    def transcribe(self, audio: str) -> List[TranscriptionSegment]:
        ...
