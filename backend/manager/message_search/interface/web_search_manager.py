from abc import ABC, abstractmethod
from backend.model.web_search.web_search_result import WebSearchResult
from typing import List


class WebSearchManager(ABC):

    @abstractmethod
    async def search(
        self,
        content: str,
        search_count: int = 5
    ) -> List[WebSearchResult]:
        ...
