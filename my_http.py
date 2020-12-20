import httpx
from typing import Optional
from response import Response


class Request(object):
    """
        请求对象
    """

    def __init__(
            self, url: str,
            callback: Optional[str] = None,
            method: str = 'GET'
    ) -> None:
        """
            构造函数
        :param url: 爬取的url
        """
        self.url = url

        self.callback = callback if callback else 'parse'

        self.method = method

    async def download(self):
        """
            异步下载
        :return:
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.url)
            except Exception as e:
                response = None
            return Response(response, callback=self.callback)