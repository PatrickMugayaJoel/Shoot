from flask import Flask
from src.app import create_app
from src.error_handlers import error_handlers
from src.database.models import setup_db
from flask_cors import CORS

app = Flask(__name__)
setup_db(app)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    """ configuring CORS"""
    response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
    return response

create_app(app)
error_handlers(app)
