from flask import Flask

def create_app():
    app = Flask(__name__)
    routes.init_app(app)
    return app

from app import routes
