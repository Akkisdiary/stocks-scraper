import re
from typing import Union

class Regex:
    PRICE = re.compile(r"([+-.]?\d\d*(\.\d\d?)?)")
    WHITESPACE = re.compile(r"\s+")
    TOKEN = re.compile(r"[,\$!/\\t\\n\\r]")


def parse_price(price: Union[str,int,float]):
    if isinstance(price, (float, int)):
        return float(price)

    price = Regex.WHITESPACE.sub(" ", price).strip()
    price = Regex.TOKEN.sub("", price).strip()

    if price:
        price = Regex.PRICE.search(price).group(1)
        return float(price)

