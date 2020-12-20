from __future__ import absolute_import


import click
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from controller._controller import Controller


@click.command()
@click.option('--crawl', help='start crawl')
def crawl(crawl):
    """开始爬取的任务"""

    # 获取到需要运行的文件名
    controller = Controller(crawl)
    controller.start()


if __name__ == '__main__':
    crawl()