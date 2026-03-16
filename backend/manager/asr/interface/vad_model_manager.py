from abc import ABC, abstractmethod
from typing import List
from model.asr.timestamp import TimeStamp


class VadModelManager(ABC):
    @abstractmethod
    def separate(self, audio: str) -> List[TimeStamp]:
        ...
