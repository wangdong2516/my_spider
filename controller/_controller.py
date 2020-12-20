import asyncio
import importlib
import inspect
from pathlib import Path
from spider import Spider


class Controller(object):
    """
        流程控制类，将会被自定义命令所调用,调用对应的脚本
    """

    def __init__(self, filename):
        """

        :param filename:
        """
        self.filename = filename

    def start(self):
        # 导入模块
        module_obj = importlib.import_module(self.filename)
        # 获取模块下所有的类
        cls = inspect.getmembers(module_obj, inspect.isclass)

        # 获取Spider的子类并且调用该子类的方法
        for i, k in cls:
            if issubclass(k, Spider) and k != Spider:
                # 实例化
                obj = k()
                # 获取请求结果
                response_list = asyncio.run(k.start_requests(obj))
                # 调用对应的方法
                for response in response_list:
                    callback = response.callback
                    if getattr(obj, callback):
                        func = getattr(obj, callback)
                        result = func(response)
                        print(result)