from manager.asr.interface.vad_model_manager import VadModelManager
from model.asr.timestamp import TimeStamp
from typing import List
from silero_vad import load_silero_vad, get_speech_timestamps


class SileroVadModelManager(VadModelManager):
    def __init__(self) -> None:
        self.model = load_silero_vad()

    def separate(self, audio: str) -> List[TimeStamp]:
        ...
