from pydantic import BaseModel


class FormatSegment(BaseModel):
    start: float
    end: float
    text: str
    translate_text: str | None = None
