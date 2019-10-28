import os
from flask import Flask
from src.views.movies import movies_app
from src.views.actors import actors_app
from src.error_handlers import error_handlers
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

database_path = os.environ['DATABASE_URL']

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from src.database import setup_db
setup_db()

from .database.dummy_data import AddDbData
AddDbData()

CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    """ configuring CORS"""
    response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return "Welcome to Capstone."

movies_app(app)
error_handlers(app)
