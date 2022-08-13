from lxml import html
from lxml.html import HtmlElement


def parse_html(text: str) -> HtmlElement:
    return html.fromstring(text)


def extract(elem: HtmlElement, xpath: str, index: int=None):
    results = elem.xpath(xpath)

    if index is not None:
        if len(results) > 0: return results[index]
        return
    return results
