import json
from typing import Any, Dict, List, Union

from . import http
from .utils import parse_price

remote = "https://scanner.tradingview.com/global/scan"
DEFAULT_MARKETS = [
    "america",
    "uk",
    "india",
    "spain",
    "russia",
    "australia",
    "brazil",
    "japan",
    "newzealand",
    "turkey",
    "switzerland",
    "hongkong",
    "taiwan",
    "netherlands",
    "belgium",
    "portugal",
    "france",
    "mexico",
    "canada",
    "colombia",
    "uae",
    "nigeria",
    "singapore",
    "germany",
    "peru",
    "poland",
    "italy",
    "argentina",
    "israel",
    "egypt",
    "serbia",
    "chile",
    "china",
    "malaysia",
    "ksa",
    "bahrain",
    "qatar",
    "indonesia",
    "finland",
    "iceland",
    "denmark",
    "romania",
    "hungary",
    "sweden",
    "slovakia",
    "lithuania",
    "luxembourg",
    "estonia",
    "latvia",
    "vietnam",
    "rsa",
    "thailand",
    "korea",
    "norway",
    "philippines",
    "greece",
    "venezuela",
]


def search_payload(
    query: str, markets: List[str] = DEFAULT_MARKETS, limit: int = 10
) -> Dict[str, Any]:
    return {
        "filter": [
            {"left": "market_cap_basic", "operation": "nempty"},
            {"left": "is_primary", "operation": "equal", "right": True},
            {"left": "name,description", "operation": "match", "right": query},
        ],
        "options": {"lang": "en"},
        "markets": markets,
        "symbols": {"query": {"types": []}, "tickers": []},
        "columns": [
            "name",
            "description",
            "close",
            "sector",
            "industry",
            "fundamental_currency_code",
            "exchange",
            "country",
        ],
        "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc"},
        "price_conversion": {"to_symbol": True},
        "range": [0, limit],
    }


def search(query: str) -> List[Dict[str, str]]:
    payload = search_payload(query)
    headers = {
        "accept": "text/plain, */*; q=0.01",
        "accept-language": "en",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.tradingview.com",
        "referer": "https://www.tradingview.com/",
    }
    data = http.json(remote, "POST", data=json.dumps(payload), headers=headers)

    results = []

    items = data.get("data")

    for item in items:
        id = item.get("s")
        symbol, name, price, sector, industry, currency, exchange, country = item.get(
            "d"
        )

        url = f"https://www.tradingview.com/symbols/{symbol.replace(':','-')}/"

        results.append(
            {
                "id": id,
                "symbol": symbol,
                "name": name,
                "price": parse_price(price),
                "sector": sector,
                "industry": industry,
                "currency": currency,
                "exchange": exchange,
                "country": country,
                "url": url,
            }
        )

    return results


def detail(url: str) -> Dict[str, Union[str, float]]:
    raise NotImplementedError("TradingView detail extraction not implemented")


def currency_payload(code: str):
    return {
        "filter": [
            {"left": "name", "operation": "nempty"},
            {"left": "name,description", "operation": "match", "right": code},
        ],
        "options": {"lang": "en"},
        "markets": ["forex"],
        "symbols": {"query": {"types": ["forex"]}, "tickers": []},
        "columns": [
            "name",
            "close",
            "description",
        ],
        "sort": {"sortBy": "name", "sortOrder": "asc"},
        "range": [0, 300],
    }


def currency(code: str):
    payload = currency_payload(code)
    headers = {
        "accept": "text/plain, */*; q=0.01",
        "accept-language": "en",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.tradingview.com",
        "referer": "https://www.tradingview.com/",
    }
    data = http.json(remote, "POST", data=json.dumps(payload), headers=headers)

    results = []

    items = data.get("data")

    for item in items:
        id = item.get("s")
        name, close, description = item.get("d")

        from_code = name[:3]
        to_code = name[-3:]

        desc = description.split("/")
        from_name = desc[0].strip()
        to_name = desc[-1].strip()

        results.append(
            {
                "id": id,
                "from": {
                    "name": from_name,
                    "code": from_code,
                },
                "to": {
                    "name": to_name,
                    "code": to_code,
                },
                "rate": close,
            }
        )

    return results


def random_stocks(limit: int = 10):
    payload = search_payload("", ["india"])
    headers = {
        "accept": "text/plain, */*; q=0.01",
        "accept-language": "en",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.tradingview.com",
        "referer": "https://www.tradingview.com/",
    }
    data = http.json(remote, "POST", data=json.dumps(payload), headers=headers)

    results = []

    items = data.get("data")

    for item in items:
        id = item.get("s")
        symbol, name, price, sector, industry, currency, exchange, country = item.get(
            "d"
        )

        url = f"https://www.tradingview.com/symbols/{symbol.replace(':','-')}/"

        results.append(
            {
                "id": id,
                "symbol": symbol,
                "name": name,
                "price": parse_price(price),
                "sector": sector,
                "industry": industry,
                "currency": currency,
                "exchange": exchange,
                "country": country,
                "url": url,
            }
        )

    return results
