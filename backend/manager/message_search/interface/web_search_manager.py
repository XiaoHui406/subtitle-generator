from abc import ABC, abstractmethod
from model.web_search_result import WebSearchResult
from typing import List


class WebSearchManager(ABC):

    @abstractmethod
    async def search(
        self,
        content: str,
        search_count: int = 10
    ) -> List[WebSearchResult]:
        ...
