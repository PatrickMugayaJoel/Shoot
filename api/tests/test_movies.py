import os
from flask import Flask
from functools import wraps
from unittest.mock import patch
import unittest
import json
from src import app
from src.error_handlers import error_handlers
from flask_sqlalchemy import SQLAlchemy


def mock_func(x=''):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            payload = x
            return f(payload, *args, **kwargs)
        return wrapper
    return decorator

""" overiding requires_auth decorator """
patch('src.views.movies.requires_auth', mock_func).start()
from src.views.movies import movies_app

test_app = Flask(__name__)
movies_app(test_app)
error_handlers(test_app)

class MoviesTestCase(unittest.TestCase):

    def setUp(self):
        self.client = test_app.test_client()

    def test_get_movies(self):
        """ Test get movies endpoint """
        response = self.client.get('/movies')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(body['movies'], list))

    def test_delete_movies(self):
        """ Test delete movies endpoint """
        response = self.client.delete('/movies/1')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['message'], 'Movie Successfully deleted.')

    def test_post_movies(self):
        """ Test post movies endpoint """
        body = {
            "release_date": "2020/06/11",
            "title": "test"
        }
        response = self.client.post('/movies',
                                    content_type='application/json',
                                    data=json.dumps(body))
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(body['movie']['title'], 'test')

    def test_patch_movies(self):
        """ Test update movies endpoint """
        body = {
            "title": "patch"
        }
        response = self.client.patch('/movies/2',
                                    content_type='application/json',
                                    data=json.dumps(body))
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['movie']['title'], 'patch')

    ##################
    # error behavior #
    ##################

    def test_get_movie(self):
        """ Test wrong endpoint """
        response = self.client.get('/movie')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(body['message'], "resource not found")

    def test_delete_movie(self):
        """ Test delete movies endpoint with unexisting id """
        response = self.client.delete('/movies/0')
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(body['message'], "resource not found")

    def test_post_movie(self):
        """ Test post movies endpoint without a title """
        body = {"release_date": "2020/06/11"}
        response = self.client.post('/movies',
                                    content_type='application/json',
                                    data=json.dumps(body))
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(body['message'], ['title should be a string.'])

    def test_patch_movie(self):
        """ Test update movies endpoint with integer as title """
        body = {"title": 1000}
        response = self.client.patch('/movies/2',
                                    content_type='application/json',
                                    data=json.dumps(body))
        body = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(body['message'], ['title should be a string.'])


if __name__ == "__main__":
    unittest.main()
