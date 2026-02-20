from typing import List, Dict
from model.format_segment import FormatSegment
from manager.output_format.interface.base_formatter import BaseFormatter
import json


class JsonFormatter(BaseFormatter):
    def format(
        self,
        segments: List[FormatSegment],
        include_text: bool,
        include_translate_text: bool
    ) -> str:
        lines: List[Dict] = []
        for seg in segments:
            item: Dict[str, str | float | None] = {
                "start": seg.start, "end": seg.end}
            if include_text:
                item["text"] = seg.text
            if include_translate_text:
                item["translate_text"] = seg.translate_text
            lines.append(item)
        return json.dumps(lines, ensure_ascii=False)
