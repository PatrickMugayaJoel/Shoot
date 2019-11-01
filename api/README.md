# Shoot Backend API

Shoot is a casting agency that creates movies, manages and assigns actors to the movies.

## Demo

[Demo application](https://shoot-agency-api.herokuapp.com/)

## Pre-requirements

* Install latest version of [python](https://www.python.org/downloads/)
* Create an [Auth0](https://auth0.com/) application with the roles described under Roles & Permissions [here](https://github.com/PatrickMugayaJoel/Shoot/blob/develop/README.md).
    Fomart permissions as: 'view:actors', 'view:movies', 'delete:actors', 'add:actors', 'update:actors', 'update:movies', 'delete:movies' and 'add:movies'.

## Installation

Clone this [repository](https://github.com/PatrickMugayaJoel/Shoot.git).
* Add a local environment file.
    ```
    # api/.env
    export AUTH0_DOMAIN='' # eg myapp.auth0.com
    export AUTH0_API_AUDIENCE='' # auth0 audience
    export DATABASE_URL="" # eg: postgresql://user:password@host:port/dbname
    export TEST_DATABASE_URL=""
    export FLASK_ENV=''
    export FLASK_APP=run.py
    ```
* Open `api` directory in the terminal.
* Install a [virtual environment](https://virtualenv.pypa.io/en/latest/) and activate it.
* Run `pip3 install -r requirements.txt` to install dependencies.
* Run the bash file `setup.sh` to setup & start the flask api server.
* The app will by default be served on port: 5000

## Unit testing

* Install the Api as directed in the installation section above.
* Stop the server or on a new terminal run the bash file `test.sh`.

## Endpoints

All endpoints require a jwt token with a prefix `Bearer` and contains user permissions.

| REQUEST TYPE | ROUTE | ACCESS PERMISSION | TASK | BODY |
| ------------- | ----- | ------------- | ------------- | ------------- |
| POST | /movies | add:movies | Add a movie| { title:"String", release_date:"String" } |
| PATCH | /movies/id | update:movies | Update a movie| { title:"optional String", release_date:"optional String" } |
| GET | /movies | view:movies | Get movies | N/A |
| DELETE | /movies/id | delete:movies | Delete a movie | N/A |
| POST | /actors | add:actors | Add an actor | { name:"String", age:"Number", gender:"String" } |
| PATCH | /actors/id | update:actors | Update an actor | { name:"optional String", age:"optional Number" gender:"optional String" } |
| GET | /actors | view:actors | Get actors| N/A |
| DELETE | /actors/id | delete:actors | delete an actor | N/A |

## Responses

### Success responses

| END POINT | CODE | RESPONSE BODY |
| ------------- | ----- | ------------- |
| POST:/movies | 201 | { 'success': True, 'movie': { title:"String", release_date:"String" } } |
| PATCH:/movies/id | 200 | { 'success': True, 'movie': { title:"String", release_date:"String" } } |
| GET:/movies | 200 | { 'movies': [{ title:"String", release_date:"String" }, ...] }|
| DELETE:/movies/id | 200 | { 'success': True, 'message': 'Movie Successfully deleted.' } |
| POST:/actors | 201 | { 'success': True, 'actor': { name:"String", age:"Number", gender:"String" } } |
| PATCH:/actors/id | 200 | { 'success': True, 'actor': { name:"String", age:"Number", gender:"String" } } |
| GET:/actors | 200 | { 'actors': [{ name:"String", age:"Number", gender:"String" }, ...] }|
| DELETE:/actors/id | 200 | { 'success': True, 'message': 'Actor Successfully deleted.' } |

### Error responses

| RESPONSE CODE | RESPONSE BODY |
| ------------- | ----- |
| 401 | { "success": False, "error": 401, "message": { 'code': 'String', 'description': 'String' } } |
| http_status_code | { "success": False, "error": http_status_code, "message": "String" } |

## Author

mugayajoelpatrick@gmail.com

## Acknowledgments

* Udacity
