from pydantic import BaseModel
from typing import Dict, Any


class WebSearchResult(BaseModel):
    content: str
    metadata: Dict[str, Any]
