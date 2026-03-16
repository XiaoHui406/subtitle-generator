from pydantic import BaseModel
from typing import List


class ASRModelConfig(BaseModel):
    id: int
    name: str
    provider: str
    type: str
    size: str
    support_languages: List[str]
    min_vram_gb: float
    description: str


class ASRModelJsonConfig(BaseModel):
    version: str
    last_updated: str
    models: List[ASRModelConfig]
