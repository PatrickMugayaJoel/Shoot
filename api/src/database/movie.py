from . import db, actor_movie
from .helper import helper


'''
Movie model
'''
class Movie(db.Model, helper):  
  __tablename__ = 'movies'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(120), nullable=False)
  release_date = db.Column(db.String(120), nullable=False)
  actors = db.relationship("Actor", secondary=actor_movie)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
    }

  def __repr__(self):
      return f"<Movie: {self.title}>"
