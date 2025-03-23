from flask import request
from flask_restful import Resource

from ...crawler import tradingview
from .utils import response


class CurrencyResource(Resource):
    def get(self, code: str):
        data = tradingview.currency(code)
        return response({"data": data}, 200)
