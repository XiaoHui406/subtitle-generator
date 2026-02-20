from pydantic import BaseModel
from typing import List
from model.format_segment import FormatSegment


class OutputFormatRequest(BaseModel):
    output_formats: List[str]
    segments: List[FormatSegment]
    include_text: bool = True
    include_translate_text: bool = True


class OutputFormatResponse(BaseModel):
    output_format: str
    formated_text: str
