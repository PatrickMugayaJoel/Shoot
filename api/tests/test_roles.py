import os
from flask import Flask
from functools import wraps
from unittest.mock import patch
import unittest
import json
from src import app
from src.error_handlers import error_handlers
from flask_sqlalchemy import SQLAlchemy
from src.auth import AuthError

class MockFunc:
    def __init__(self, payload=['view:actors', 'view:movies']):
        self.payload = payload
            
    def requires_auth(self, x=''):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                if x not in self.payload:
                    raise AuthError({
                        'code': 'unauthorized',
                        'description': 'Permission not found.'
                    }, 403)
                return f(self.payload, *args, **kwargs)
            return wrapper
        return decorator

casting_assistant = MockFunc()
patch('src.views.actors.requires_auth', casting_assistant.requires_auth).start()
from src.views.actors import actors_app

casting_assistant_app = Flask(__name__)
actors_app(casting_assistant_app)
error_handlers(casting_assistant_app)


casting_director = MockFunc(
    ['view:actors', 'view:movies', 'delete:actors', 'add:actors', 'update:movies', 'update:actors']
)
patch('src.views.movies.requires_auth', casting_director.requires_auth).start()
from src.views.movies import movies_app

casting_director_app = Flask(__name__)
movies_app(casting_director_app)
error_handlers(casting_director_app)


executive_producer = MockFunc(
    ['view:actors', 'view:movies', 'delete:actors', 'add:actors', 'update:actors', 'update:movies', 'delete:movies', 'add:movies']
)
patch('src.views.movies.requires_auth', executive_producer.requires_auth).start()
from src.views.movies import movies_app

executive_producer_app = Flask(__name__)
movies_app(executive_producer_app)
error_handlers(executive_producer_app)


class ActorsTestCase(unittest.TestCase):

    def setUp(self):
        self.casting_assistant_client = casting_assistant_app.test_client()
        self.casting_director_client = casting_director_app.test_client()
        self.executive_producer_client = executive_producer_app.test_client()

    def test_get_actors(self):
        """ Test casting assistant get actors endpoint """
        response = self.casting_assistant_client.get('/actors')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(body['actors'], list))

    def test_delete_actors(self):
        """ Test casting assistant delete actor endpoint """
        response = self.casting_assistant_client.delete('/actors/1')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(body['message']['error']['code'], 'unauthorized')

    def test_patch_movies(self):
        """ Test casting producer update movies endpoint """
        body = {
            "title": "patch"
        }
        response = self.casting_director_client.patch('/movies/2',
                                    content_type='application/json',
                                    data=json.dumps(body))
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['movie']['title'], 'patch')

    def test_delete_movies(self):
        """ Test casting producer delete movies endpoint """
        response = self.casting_director_client.delete('/movies/1')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(body['message']['error']['code'], 'unauthorized')

    def test_patch_movie(self):
        """ Test casting producer update movies endpoint """
        body = {
            "title": "executive"
        }
        response = self.executive_producer_client.patch('/movies/2',
                                    content_type='application/json',
                                    data=json.dumps(body))
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['movie']['title'], 'executive')

    def test_delete_movie(self):
        """ Test casting producer delete movies endpoint """
        response = self.executive_producer_client.delete('/movies/3')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['message'], 'Movie Successfully deleted.')


if __name__ == "__main__":
    unittest.main()
