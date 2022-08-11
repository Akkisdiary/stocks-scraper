from flask import request
from flask_restful import Resource

from ... import crawler
from .utils import response


class DetailResource(Resource):
    def get(self):
        url = request.args.get("url")

        if not url:
            status_code = 400
            return response({"message": "detail url not provided"}, status_code)
        
        data = crawler.detail(url)
        return response(data, 200)
