from . import db, actor_movie
from .helper import helper

'''
Actor model
'''
class Actor(db.Model, helper):  
  __tablename__ = 'actors'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  movies = db.relationship("Movie", secondary=actor_movie)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  
  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }

  def __repr__(self):
      return f"<Actor: {self.name}>"
