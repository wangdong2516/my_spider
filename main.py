import asyncio
from response import Response
# import time
#
#
# async def func():
#     print(f"started at {time.strftime('%X')}")
#     print('hello')
#     # await一个协程，一般用于在一个协程中调用另一个协程
#     await asyncio.sleep(1)
#     print('world')
#     print(f"finished at {time.strftime('%X')}")
#
#
# async def say_after(delay, what):
#     # 使用result参数
#     return await asyncio.sleep(delay, result=what)
#
#     # print(what)
#
# # 执行时间3秒
# # async def main():
# #     print(f"started at {time.strftime('%X')}")
# #     await say_after(1, "hello")
# #     await say_after(2, "world")
# #     print(f"finished at {time.strftime('%X')}")
#
# """
#     如果能够在await表达式中使用，那么这个对象就是可等待对象
#     主要存在三种类型的可等待对象：
#         1. 协程
#             协程函数指的是使用async def语法定义的函数
#             协程对象指得是协程函数返回的对象
#         2. Task对象
#         3. Future对象
#
#     运行协程的三种方式:
#         1. asyncio.run() 函数用来运行最高层级的入口点 "main()" 函数
#         2. asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程
#         3. asyncio.gather()用来并发的运行多个任务，如果 aws序列中的某个可等待对象为协程，它将自动作为一个任务加入日程。
#             如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。
#             如果 return_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。
#             如果 return_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
# """
#
#
# def callback(f):
#     print(f)
#     print('1')
#
#
# async def eternity():
#     # Sleep for one hour
#     # 保护一个可等待对象，防止其被取消
#     await asyncio.shield(asyncio.sleep(10))
#     print('yay!')
#
# # 运行时间2秒
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     # 当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，该协程将自动排入日程准备立即运行:
#     # task1 = asyncio.create_task(say_after(1, "hello"))
#     task1 = await asyncio.create_task(say_after(1, "hello"))
#     task2 = await asyncio.create_task(say_after(2, "world"))
#     # 等待一个可等待对象执行完成，如果指定了timeout参数(不为None)将会在timeout指定的秒数之后引发TimeoutError
#     # await asyncio.wait_for(eternity(), timeout=None)
#     done, pending = await asyncio.wait([eternity()])
#     print(done, pending)
#     print(task1, task2)
#     # task1.add_done_callback(callback)
#     # task2.add_done_callback(callback)
#     print(f"finished at {time.strftime('%X')}")
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         if number == 4:
#             raise Exception
#
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     # return number
#     # print(f"Task {name}: factorial({number}) = {f}")
#
#
# async def division(divisor, dividend):
#     if divisor == 0:
#         raise ZeroDivisionError
#     else:
#         await asyncio.sleep(divisor)
#         print(f"{dividend}/{divisor}={dividend/divisor}")
#         return dividend/divisor
#
#
# async def do_something():
#     print('do something')
#
#
# async def main1():
#     return asyncio.shield(do_something())
#
# async def main2():
#     t1 = asyncio.create_task(main1())
#     t2 = asyncio.create_task(main1())
#     await asyncio.gather(t1, t2)
#     t1.cancel()
#
#
# asyncio.run(main2())
# async def scrapy():
#     # Schedule three calls *concurrently*:
#     task1 = asyncio.create_task(division(0, 2))
#     task2 = asyncio.create_task(division(1, 5))
#     task3 = asyncio.create_task(division(3, 6))
#     t = asyncio.gather(
#         task1,
#         task2,
#         task3,
#         return_exceptions=True
#     )
#     await t
#     print(task2.result(), task3.result())
#     # await t
# # asyncio.run(scrapy())
#
#
# # if __name__ == '__main__':
# #     # 运行协程的机制，使用run函数运行，一般用于最顶层的入口函数
# #     # asyncio.run(func())
# #     # 此函数会运行传入的协程，负责管理 asyncio 事件循环，终结异步生成器，并关闭线程池
# #     # 当有其他 asyncio 事件循环在同一线程中运行时，此函数不能被调用。
# #     asyncio.run(main())
# #     asyncio.gather(main())

from spider import Spider


class MySpider(Spider):

    name = 'baidu'

    start_urls = ['https://www.lagou.com/beijing']

    def parse(self, response: Response):
        """

        :param response: Response对象
        :return:
        """
        item = response.xpath('//div[@class="menu_sub dn"]//a/h3/text()').extract()
        return item

