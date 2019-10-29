from flask import Flask, request, jsonify, abort
from src.auth import requires_auth
from src.database.movie import Movie
from .util import validate_movie


def movies_app(app):

    @app.route('/movies')
    @requires_auth('view:movies')
    def movies(payload):
        movies = []
        for movie in Movie.query.all():
            movies.append(movie.format())
        return jsonify({
            'movies': movies
            }), 200

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        movie = Movie.query.filter_by(id=id).first()

        if not movie:
            abort(404, "Movie not found")
        movie.delete()

        return jsonify({
            'success': True,
            'message': 'Movie Successfully deleted.'
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('add:movies')
    def add_movie(payload):
        body = request.get_json()

        new_movie = Movie(
            title=body.get("title"),
            release_date=body.get("release_date")
        )

        is_valid = validate_movie(new_movie)

        if not (is_valid is True):
            abort(400, is_valid)

        new_movie.insert()
        return jsonify({
            'success': True,
            'movie': new_movie.format()
        }), 201

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(payload, id):
        body = request.get_json()
        movie = Movie.query.filter_by(id=id).first()

        if not movie:
            abort(404)

        movie.title = body.get("title", movie.title)
        movie.release_date = body.get("release_date", movie.release_date)

        is_valid = validate_movie(movie)

        if not (is_valid is True):
            abort(400, is_valid)

        movie.update()
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 201
