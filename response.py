from lxml import etree
from selector import Selector


class Response(object):

    def __init__(self, response, callback='parse'):
        if response:
            self.content = response.text
        else:
            self.content = ''
        self.callback = callback

    def to_html(self):
        """
            转换为html对象
        :return:
        """
        return etree.HTML(self.content)

    def xpath(self, xpath_expr: str):
        """
            xpath语法
        :return:
        """
        selector = Selector(self.content, xpath_expr=xpath_expr)
        return selector
