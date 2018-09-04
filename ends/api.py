import logging

from sqlalchemy import create_engine
from flask import Flask
from flask_restful import Api

from ends.resources import Data, Health

def create_app():
    db = create_engine('sqlite:///chinook.db')
    app = Flask(__name__)
    api = Api(app)
    version = '/v0'
    api.add_resource(Data, version + '/data/<int:userId>')
    api.add_resource(Health, '/health')

    return app, db
