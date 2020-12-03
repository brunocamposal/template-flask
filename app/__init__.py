from flask import Flask, Blueprint
from app.views.index_views import bp as index_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index_bp)

    return app