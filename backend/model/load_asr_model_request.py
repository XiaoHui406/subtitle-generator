from pydantic import BaseModel


class LoadASRModelRequest(BaseModel):
    model_name: str
    device: str | None = None
