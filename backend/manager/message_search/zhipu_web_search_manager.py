import httpx
from manager.message_search.interface.web_search_manager import WebSearchManager
from typing import List, Dict
from model.web_search_result import WebSearchResult


class ZhipuWebSearchManager(WebSearchManager):
    def __init__(
        self,
        apikey: str
    ) -> None:
        self.apikey: str = apikey

    async def search(
        self,
        content: str,
        search_count: int = 5
    ) -> List[WebSearchResult]:
        async with httpx.AsyncClient() as client:
            search_result = await client.post(
                url='https://open.bigmodel.cn/api/paas/v4/web_search',
                headers={
                    "Authorization": f"Bearer {self.apikey}",
                    "Content-Type": "application/json"
                },
                json={
                    "search_engine": "search-std",
                    "search_intent": False,
                    "search_query": content,
                    "count": search_count
                }
            )
        search_response: Dict = search_result.json()
        result: List[WebSearchResult] = []
        for item in search_response['search_result']:
            result.append(
                WebSearchResult(
                    content=f'id={item['refer']}, title={item['title']} content={item['content']}',
                    metadata={
                        "id": item['refer'],
                        "title": item['title'],
                        "content": item['content']
                    }
                )
            )
        return result
