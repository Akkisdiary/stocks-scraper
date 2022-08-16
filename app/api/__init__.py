from flask_restful import Api

from .resources import DetailResource, SearchResource


def create_api():
    api = Api()
    
    api.add_resource(SearchResource, "/search")
    # api.add_resource(DetailResource, "/detail")

    return api
