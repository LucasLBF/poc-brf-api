from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={"/": {"origins": "*", "content-type": "application/json"}})
    routes.init_app(app)
    return app

from app import routes
