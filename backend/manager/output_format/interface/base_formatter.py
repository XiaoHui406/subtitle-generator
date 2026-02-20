from abc import ABC, abstractmethod
from model.format_segment import FormatSegment
from typing import List


class BaseFormatter(ABC):

    @abstractmethod
    def format(
        self,
        segments: List[FormatSegment],
        include_text: bool,
        include_translate_text: bool
    ) -> str:
        ...
