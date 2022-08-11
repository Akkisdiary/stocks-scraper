import json
from typing import Dict, List, Union

from furl import furl

from .http import text
from .scraper import extract, parse_html


def search(query: str) -> List[Dict[str, str]]:
    remote = furl("https://www.investing.com/search/")
    remote.args["q"] = query
    
    doc = parse_html(text(remote.url))
    
    results = []

    items = extract(doc, "//div[@class='searchSectionMain']//a[contains(@class,'results-quote-item')]")
    for item in items:
        url = extract(item, "./@href", 0)
        name = extract(item, ".//*[@class='third']/text()", 0)
        symbol = extract(item, ".//*[@class='second']/text()", 0)
        exchange = extract(item, ".//*[@class='fourth']/text()", 0)

        if url is not None:
            if not url.startswith("http"):
                url = remote.origin + url
            url += '-company-profile'

            results.append({
                "url": url,
                "name": name,
                "symbol": symbol,
                "exchange": exchange,
            })

    return results
    
    
def detail(url: str) -> Dict[str, Union[str, float]]:
    doc = parse_html(text(url))
    
    data = {
        'url': url,
        'price': extract(doc, "//*[@id='last_last']/text()", 0),
        'industry': extract(doc, "//div[text()='Industry']/a/text()", 0),
        'sector': extract(doc, "//div[text()='Sector']/a/text()", 0),
        'market': extract(doc, "//div[contains(@class,'general-info')]//div[span[contains(text(),'Market')]]/span[@class='elp']/@title", 0),
    }
    script = extract(doc, "//script[contains(text(),'tickersymbol')]/text()", 0)
    if script:
        try:
            json_data = json.loads(script)
            data.update({
                'name': json_data.get('legalName'),
                'symbol': json_data.get('tickersymbol'),
                'country': json_data.get('Address',{}).get("addresscountry",{}).get("name"),
            })
        except ValueError:
            pass

    return data
