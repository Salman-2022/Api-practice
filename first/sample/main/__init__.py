from flask import Flask
from flask_restful import Api
from sample import app


api = Flask(__name__)
api = Api(app)