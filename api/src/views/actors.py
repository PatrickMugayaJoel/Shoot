from flask import Flask, request, jsonify, abort
from src.auth import requires_auth
from src.database.actor import Actor
from .util import validate_actor


def actors_app(app):

    @app.route('/actors')
    def actors():
        actors = []
        for actor in Actor.query.all():
            actors.append(actor.format())
        return jsonify({
            'actors': actors
            }), 200

    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        actor = Actor.query.filter_by(id=id).first()

        if not actor:
            abort(404, "Actor not found")
        actor.delete()

        return jsonify({
            'success': True,
            'message': 'Actor Successfully deleted.'
        }), 200

    @app.route('/actors', methods=['POST'])
    def add_actor():
        body = request.get_json()

        new_actor = Actor(
            name=body.get("name"),
            age=body.get("age"),
            gender=body.get("gender")
        )

        is_valid = validate_actor(new_actor)

        if not (is_valid is True):
            abort(400, is_valid)

        new_actor.insert()
        return jsonify({
            'success': True,
            'movie': new_actor.format()
        }), 201

    @app.route('/actors/<int:id>', methods=['PATCH'])
    def update_actor(id):
        body = request.get_json()
        actor = Actor.query.filter_by(id=id).first()

        if not actor:
            abort(404)

        actor.name = body.get("name", actor.name)
        actor.age = body.get("age", actor.age)
        actor.gender = body.get("gender", actor.gender)

        is_valid = validate_actor(actor)

        if not (is_valid is True):
            abort(400, is_valid)

        actor.update()
        return jsonify({
            'success': True,
            'movie': actor.format()
        }), 201
