#
# import click
# from pathlib import Path
# import sys
# from importlib import import_module
# # module = import_module(str(parent_dir / 'controller'))
# # print(module)
#
# @click.command()
# @click.option('--crawl', help='start crawl')
# def crawl(crawl):
#     """开始爬取的任务"""
#
#     # 获取到需要运行的文件名
#     parent_dir = Path(__file__).parent.parent
#     print(parent_dir)
#
#     import_module(str(parent_dir / '_controller.py'))
#     # module = import_module(str(parent_dir / 'controller'))
#     # controller = Controller(filename)
#     # controller.start()
#
#
# if __name__ == '__main__':
#     crawl()