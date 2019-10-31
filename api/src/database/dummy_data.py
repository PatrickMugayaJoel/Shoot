from . import db
from .actor import Actor
from .movie import Movie


class AddDbData():
    actor1 = Actor("Joel", 30, "male")
    db.session.add(actor1)
    db.session.commit()

    movie1 = Movie("The Watch men", "2018-02-02")
    movie2 = Movie("Black Panther", "2017-06-14")
    movie3 = Movie("Thor", "2018-10-04")

    db.session.add(movie3)
    db.session.commit()

    actor2 = Actor("Patrick", 13, "male")
    actor2.movies = [movie1]
    db.session.add(actor2)
    db.session.commit()

    actor3 = Actor("Joan", 22, "female")
    actor3.movies = [movie1, movie2]
    db.session.add(actor3)
    db.session.commit()

