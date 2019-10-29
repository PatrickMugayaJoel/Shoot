from flask import Flask, jsonify
from .auth import AuthError


def error_handlers(app):

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal error and was unable to complete your request."
        }), 500


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(405)
    def invalid_method(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": error.description
        }), 405


    @app.errorhandler(401)
    def permission_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authentication error"
        }), 401


    @app.errorhandler(400)
    def user_error(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": error.description
        }), 400


    @app.errorhandler(AuthError)
    def invalid_claims(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": error.__dict__
        }), 401
