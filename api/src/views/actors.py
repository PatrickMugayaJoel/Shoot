from flask import Flask, request, jsonify, abort
from src.auth import requires_auth
from src.database.actor import Actor
from .util import validate_actor


def actors_app(app):

    @app.route('/actors')
    @requires_auth('view:actors')
    def actors(payload):
        actors = []
        for actor in Actor.query.all():
            actors.append(actor.format())
        return jsonify({
            'actors': actors
            }), 200

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.filter_by(id=id).first()

        if not actor:
            abort(404, "Actor not found")
        actor.delete()

        return jsonify({
            'success': True,
            'message': 'Actor Successfully deleted.'
        }), 200

    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(payload):
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
            'actor': new_actor.format()
        }), 201

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(payload, id):
        actor = Actor.query.filter_by(id=id).first()
        if not actor:
            abort(404)
    
        body = request.get_json()

        actor.name = body.get("name", actor.name)
        actor.age = body.get("age", actor.age)
        actor.gender = body.get("gender", actor.gender)

        is_valid = validate_actor(actor)

        if not (is_valid is True):
            abort(400, is_valid)

        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200
