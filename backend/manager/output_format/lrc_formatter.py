from typing import List
from model.format_segment import FormatSegment
from manager.output_format.interface.base_formatter import BaseFormatter


class LrcFormatter(BaseFormatter):
    def format(
        self,
        segments: List[FormatSegment],
        include_text: bool,
        include_translate_text: bool
    ) -> str:
        lines: List[str] = []
        for segment in segments:
            start = self._seconds_to_lrc_time(segment.start)
            if include_text and segment.text:
                lines.append(f"[{start}]{segment.text}")
            if include_translate_text and segment.translate_text:
                lines.append(f"[{start}]{segment.translate_text}")
        return "\n".join(lines)

    def _seconds_to_lrc_time(self, seconds: float) -> str:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        centis = int((seconds % 1) * 100)
        return f"{minutes:02d}:{secs:02d}.{centis:02d}"
