from flask_restful import Api

from .resources import CurrencyResource, SearchResource


def create_api():
    api = Api()
    
    api.add_resource(SearchResource, "/search")
    api.add_resource(CurrencyResource, "/currency/<string:code>")

    return api
