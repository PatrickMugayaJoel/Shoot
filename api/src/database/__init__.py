from src import db

actor_movie = db.Table('actor_movie',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'))
)

from .actor import Actor
from .movie import Movie

def setup_db():
    db.drop_all()
    db.create_all()
