from flask import request
from flask_restful import Resource

from ...crawler import tradingview
from .utils import response


class SearchResource(Resource):
    def get(self):
        query = request.args.get("query")

        if not query:
            status_code = 400
            return response({"message": "search query not provided"}, status_code)

        results = tradingview.search(query)
        return response({"results": results}, 200)


class SearchRandomResource(Resource):
    def get(self):
        limit = request.args.get("query") or "10"

        if not limit.isdigit():
            status_code = 400
            return response({"message": "please provide an integer limit"}, status_code)

        results = tradingview.random_stocks(int(limit))
        return response({"results": results}, 200)
