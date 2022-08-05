# from flask import Flask,jsonify,request
# from flask_restful import Resource,Api
from sample import api
from sample.controler.user_controller import Hello,Square

api.add_resource(Hello,'/')
api.add_resource(Square,'/square/<int:num>')