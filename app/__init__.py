from flask import Flask

from .api import create_api


def create_app():
    app = Flask(__name__)

    api = create_api()
    api.init_app(app)
    
    with app.app_context():
        return app
