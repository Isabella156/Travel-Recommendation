from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)

# cors
CORS(app, resource=r'/*/')

# configuration
app.config['WTF_CSRF_ENABLED'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../Place/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

# create database
db = SQLAlchemy(app)

# api manager
apis = Api(app)

# jsonify
ma = Marshmallow(app)

# database migration
migrate = Migrate(app, db)

from app import models, api, views

# route
apis.add_resource(api.GetPlaceImages, '/images/<placeid>')
