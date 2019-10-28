from . import db
from .actor import Actor
from .movie import Movie


class AddDbData():
    actor1 = Actor("Joel", 30, "male")
    db.session.add(actor1)
    db.session.commit()

    movie1 = Movie("The Watch men", "2019/08/02")
    movie2 = Movie("Black Panther", "2018/06/11")

    actor2 = Actor("Patrick", 13, "male")
    actor2.movies = [movie1]
    db.session.add(actor2)
    db.session.commit()

    actor3 = Actor("Joan", 22, "female")
    actor3.movies = [movie1, movie2]
    db.session.add(actor3)
    db.session.commit()

