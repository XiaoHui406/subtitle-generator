from typing import List
from model.format_segment import FormatSegment
from manager.output_format.interface.base_formatter import BaseFormatter


class TsvFormatter(BaseFormatter):
    def format(
        self,
        segments: List[FormatSegment],
        include_text: bool,
        include_translate_text: bool
    ) -> str:
        headers = ["start", "end"]
        if include_text:
            headers.append("text")
        if include_translate_text:
            headers.append("translate_text")
        lines: List[str] = ["\t".join(headers)]

        for segment in segments:
            start_ms = int(segment.start * 1000)
            end_ms = int(segment.end * 1000)
            cols = [str(start_ms), str(end_ms)]
            if include_text and segment.text:
                cols.append(segment.text)
            if include_translate_text and segment.translate_text:
                cols.append(segment.translate_text)
            lines.append("\t".join(cols))
        return "\n".join(lines)
