from typing import List, Dict
from backend.model.web_search.web_search_result import WebSearchResult
from message_search.interface.web_search_manager import WebSearchManager
import httpx


class NeteaseMusicWebSearchManager(WebSearchManager):
    def __init__(self) -> None:
        pass

    async def search(
        self,
        content: str,
        search_count: int = 5
    ) -> List[WebSearchResult]:
        ...
