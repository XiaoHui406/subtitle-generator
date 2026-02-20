from typing import List
from model.format_segment import FormatSegment
from manager.output_format.interface.base_formatter import BaseFormatter


class TxtFormatter(BaseFormatter):
    def format(
        self,
        segments: List[FormatSegment],
        include_text: bool,
        include_translate_text: bool
    ) -> str:
        text_list: List[str] = []
        for segment in segments:
            if include_text:
                text_list.append(segment.text)
            if include_translate_text and segment.translate_text:
                text_list.append(segment.translate_text)
        return '\n'.join(text_list)
