from model.format_segment import FormatSegment
from model.output_format import OutputFormatRequest, OutputFormatResponse
from typing import List, Dict
from manager.output_format.json_formatter import JsonFormatter
from manager.output_format.lrc_formatter import LrcFormatter
from manager.output_format.srt_formatter import SrtFormatter
from manager.output_format.tsv_formatter import TsvFormatter
from manager.output_format.txt_formatter import TxtFormatter
from manager.output_format.vtt_formatter import VttFormatter
from manager.output_format.interface.base_formatter import BaseFormatter


class OutputFormatManager:
    def __init__(self):
        self._format_map: Dict[str, BaseFormatter] = {
            "srt": SrtFormatter(),
            "lrc": LrcFormatter(),
            "txt": TxtFormatter(),
            "json": JsonFormatter(),
            "vtt": VttFormatter(),
            "tsv": TsvFormatter(),
        }

    def format(
        self,
        output_format_request: OutputFormatRequest
    ) -> List[OutputFormatResponse]:
        responses: List[OutputFormatResponse] = []

        output_formats: List[str] = output_format_request.output_formats
        segments: List[FormatSegment] = output_format_request.segments
        include_text: bool = output_format_request.include_text
        include_translate_text: bool = output_format_request.include_translate_text

        for output_format in output_formats:
            formatter: BaseFormatter = self._format_map[output_format]

            formatted_text: str = formatter.format(
                segments=segments,
                include_text=include_text,
                include_translate_text=include_translate_text
            )

            responses.append(
                OutputFormatResponse(
                    output_format=output_format,
                    formated_text=formatted_text
                )
            )

        return responses
