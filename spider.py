import asyncio
import httpx
from typing import List
from typing import Optional
from my_http import Request


class Spider(object):
    """
        爬虫基类
    """

    name: Optional[str] = None

    def __init__(self, name: Optional[str] = None, **kwargs) -> None:
        """
            start_url为起始爬取点
        :param start_url: list
        """

        if name is not None:
            self.name = name

        elif not getattr(self, 'name', None):
            raise ValueError(f"{type(self).__name__} must have a name")

        self.__dict__.update(kwargs)

        if not hasattr(self, 'start_urls'):
            self.start_urls = []

    async def start_requests(self):
        """
            开始请求
        :return:
        """
        task_list = list()

        if not self.start_urls and hasattr(self, 'start_url'):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")

        else:
            for url in self.start_urls:
                request = Request(url)
                task = asyncio.create_task(request.download())
                task_list.append(task)

        return await asyncio.gather(*task_list)

    def parse(self, response):
        raise NotImplementedError('parse method must Implemented by yourself')
