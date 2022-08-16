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

