
from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Actor
Have title and release year
'''
class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)

  def __init__(self, name):
    self.name = name

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name
    }

  def __repr__(self):
      return self.name
