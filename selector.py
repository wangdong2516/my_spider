from lxml import etree


class Selector(object):
    """
        选择器类
    """

    def __init__(self, content, xpath_expr):
        self.html = etree.HTML(content)
        self.xpath_expr = xpath_expr

    def extract_first(self):
        return self.html.xpath(self.xpath_expr)[0]

    def extract(self):
        return self.html.xpath(self.xpath_expr)
    #
    # def xpath(self, xpath_expr):
    #     html = etree.HTML(self.response.text)
    #     element = html.xpath(xpath_expr)
    #     return element

