
from flask import Flask
from flask_restful import Api
from resources.model import ModelResource
from model.model import threading_get_dados

def create_app():
    app = Flask(__name__)
    resources(app)
    threading_get_dados.start()
    return app

def resources(app):
    api = Api(app)
    api.add_resource(ModelResource,'/ordered-numbers')

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)