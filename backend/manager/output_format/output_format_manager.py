from model.transcription_segment import TranscriptionSegment
from typing import List
import json


class OutputFormatManager:
    def format(self, output_format: str, segments: List[TranscriptionSegment]) -> str:
        match output_format:
            case "srt":
                return self._to_srt(segments=segments)
            case "lrc":
                return self._to_lrc(segments=segments)
            case "txt":
                return self._to_txt(segments=segments)
            case "json":
                return self._to_json(segments=segments)
            case "vtt":
                return self._to_vtt(segments=segments)
            case "tsv":
                return self._to_tsv(segments=segments)
            case _:
                raise ValueError(f"Unsupported format: {output_format}")

    def _to_srt(self, segments: List[TranscriptionSegment]) -> str:
        lines: List[str] = []
        for i, segment in enumerate(segments, 1):
            start = self._seconds_to_srt_time(segment.start)
            end = self._seconds_to_srt_time(segment.end)
            lines.append(f"{i}")
            lines.append(f"{start} --> {end}")
            lines.append(segment.text)
            lines.append("")
        return "\n".join(lines)

    def _seconds_to_srt_time(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    def _to_lrc(self, segments: List[TranscriptionSegment]) -> str:
        lines: List[str] = []
        for segment in segments:
            start = self._seconds_to_lrc_time(segment.start)
            lines.append(f"[{start}]{segment.text}")
        return "\n".join(lines)

    def _seconds_to_lrc_time(self, seconds: float) -> str:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        centis = int((seconds % 1) * 100)
        return f"{minutes:02d}:{secs:02d}.{centis:02d}"

    def _to_txt(self, segments: List[TranscriptionSegment]) -> str:
        result: str = ""
        for segment in segments:
            result += f"{segment.text}\n"
        return result

    def _to_json(self, segments: List[TranscriptionSegment]) -> str:
        return json.dumps(
            [segment.__dict__ for segment in segments], ensure_ascii=False
        )

    def _to_vtt(self, segments: List[TranscriptionSegment]) -> str:
        lines: List[str] = ["WEBVTT", ""]
        for segment in segments:
            start = self._seconds_to_vtt_time(segment.start)
            end = self._seconds_to_vtt_time(segment.end)
            lines.append(f"{start} --> {end}")
            lines.append(segment.text)
            lines.append("")
        return "\n".join(lines)

    def _seconds_to_vtt_time(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"

    def _to_tsv(self, segments: List[TranscriptionSegment]) -> str:
        lines: List[str] = ["start\tend\ttext"]
        for segment in segments:
            start_ms = int(segment.start * 1000)
            end_ms = int(segment.end * 1000)
            lines.append(f"{start_ms}\t{end_ms}\t{segment.text}")
        return "\n".join(lines)
