import os
from flask import Flask
from src.error_handlers import error_handlers
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

if os.environ['FLASK_ENV'] == 'testing':
    database_path = os.environ['TEST_DATABASE_URL']
else:
    database_path = os.environ['DATABASE_URL']

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
db = SQLAlchemy(app)

from src.views.movies import movies_app
from src.views.actors import actors_app
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

actors_app(app)
movies_app(app)
error_handlers(app)
