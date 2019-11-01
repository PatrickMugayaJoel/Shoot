# Shoot Frontend App

Shoot is a casting agency that creates movies, manages and assigns actors to the movies.

## Pre-requirements

* Install latest version of [Node](https://nodejs.org/en/download/)
* Create an [Auth0](https://auth0.com/) application with the roles described under Roles & Permissions [here](https://github.com/PatrickMugayaJoel/Shoot/blob/develop/README.md).
    Fomart permissions as: 'view:actors', 'view:movies', 'delete:actors', 'add:actors', 'update:actors', 'update:movies', 'delete:movies' and 'add:movies'.

## Installation

* Clone this [repository](https://github.com/PatrickMugayaJoel/Shoot.git).
* Edit `frontend/environments/environment.ts` to include Auth0 and api settings.
* Open `frontend` directory in the terminal.
* Run `npm install` to install dependencies.
* Run `npm start` to start the angular app.
* The app will by default be served on port: 4200

## Author

mugayajoelpatrick@gmail.com
 
## Acknowledgments

* Udacity
