from pydantic import BaseModel


class TimeStamp(BaseModel):
    start: float
    end: float
