from typing import List
from model.format_segment import FormatSegment
from manager.output_format.interface.base_formatter import BaseFormatter


class VttFormatter(BaseFormatter):
    def format(
        self,
        segments: List[FormatSegment],
        include_text: bool,
        include_translate_text: bool
    ) -> str:
        lines: List[str] = ["WEBVTT", ""]
        for segment in segments:
            start = self._seconds_to_vtt_time(segment.start)
            end = self._seconds_to_vtt_time(segment.end)
            lines.append(f"{start} --> {end}")
            if include_text and segment.text:
                lines.append(segment.text)
            if include_translate_text and segment.translate_text:
                lines.append(segment.translate_text)
            lines.append("")
        return "\n".join(lines)

    def _seconds_to_vtt_time(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"
