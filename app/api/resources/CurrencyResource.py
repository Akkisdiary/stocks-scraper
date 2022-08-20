from flask import request
from flask_restful import Resource

from ...crawler import tradingview
from .utils import response


class CurrencyResource(Resource):
    def get(self, code: str):
        '''
        :returns: {
            data: [
                {
                    id: str,
                    from: {
                        name: str,
                        code: str,
                    }
                    to: {
                        name: str,
                        code: str,
                    }
                    rate: float
                },
                ...
            ]
            status_code: int
        }
        '''
        data = tradingview.currency(code)
        return response({"data": data}, 200)
