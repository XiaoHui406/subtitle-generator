from model.transcription_segment import TranscriptionSegment
from typing import List
import json


class ASROutputFormatter:

    def format(
        self,
        output_format: str,
        segments: List[TranscriptionSegment]
    ) -> str:
        match output_format:
            case 'srt':
                return self._to_srt(segments=segments)
            case 'lrc':
                return self._to_lrc(segments=segments)
            case 'txt':
                return self._to_txt(segments=segments)
            case 'json':
                return self._to_json(segments=segments)
            case 'vtt':
                return self._to_vtt(segments=segments)
            case 'tsv':
                return self._to_tsv(segments=segments)
            case _:
                raise ValueError(f"Unsupported format: {output_format}")

    def _to_srt(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_lrc(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_txt(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        result: str = ''
        for segment in segments:
            result += f'{segment.text}\n'
        return result

    def _to_json(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        return json.dumps([segment.__dict__ for segment in segments], ensure_ascii=False)

    def _to_vtt(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_tsv(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...
