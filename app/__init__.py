from flask import Flask
from flask_cors import CORS

from .api import create_api


def create_app():
    app = Flask(__name__)

    cors = CORS()
    cors.init_app(app)

    api = create_api()
    api.init_app(app)
    
    with app.app_context():
        return app
