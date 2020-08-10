import os
from flask import Flask, render_template, jsonify, request, url_for, redirect, abort, flash
from models import db, setup_db, Movie, Actor
from flask_cors import CORS
from forms import *
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__, static_folder='./build', static_url_path='/')
    app.config.from_object('config')
    setup_db(app)
    CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, DELETE, PATCH')
        return response

    def format_datetime(value, format='medium'):
        date = dateutil.parser.parse(value)
        if format == 'full':
            format = "EEEE MMMM, d, y 'at' h:mma"
        elif format == 'medium':
            format = "EE MM, dd, y h:mma"
        return babel.dates.format_datetime(date, format)

    app.jinja_env.filters['datetime'] = format_datetime

    @app.route('/')
    def get_greeting():
        return app.send_static_file('index.html')

    # @app.route('/login')
    # def login():
    #     return render_template('auth/login.html')

    @app.route('/actors')  # done
    def view_actors():
        try:
            actors = Actor.query.all()
            if actors is None:
                actors = []
                return jsonify({
                    "status code": 200,
                    "success": True,
                    "actors": actors})
            actors = [actor.format() for actor in actors]
            return jsonify({
                "status code": 200,
                "success": True,
                "actors": actors})
        except:
            abort(405)
        return abort(500)

    @app.route('/movies')  # done
    def view_movies():
        try:
            movies = Movie.query.all()
            movies = [movie.format() for movie in movies]
            return jsonify({
                "status code": 200,
                "success": True,
                "movies": movies})
        except:
            abort(405)
        return abort(500)

    @app.route('/actors/<int:id>', methods=['GET'])  # done
    @requires_auth('get:actor')
    def view_actor(jwt, id):
        actor = Actor.query.get(id)
        if actor is None:
            return abort(404)
        else:
            return jsonify({
                'success': True,
                'status code': 200,
                'actor': actor.format()
            })
        return abort(500)

    @app.route('/movies/<int:id>', methods=['GET'])  # done
    @requires_auth('get:movie')
    def view_movie(jwt, id):
        movie = Movie.query.get(id)
        if movie is None:
            return abort(404)
        else:
            return jsonify({
                'success': True,
                'status code': 200,
                'movie': movie.format()
            })
        return abort(500)

    @app.route('/actors/<int:id>', methods=['DELETE'])  # done
    @requires_auth('delete:actor')
    def remove_actor(jwt, id):
        actor = Actor.query.get(id)
        if actor is not None:
            actor.delete()
            return jsonify({
                'success': True,
                'stetus code': 200,
                'message': f"removed actor with id = {id}"
            })
        else:
            abort(404)
        return abort(500)

    @app.route('/movies/<int:id>', methods=['DELETE'])  # done
    @requires_auth('delete:movie')
    def remove_movie(jwt, id):
        movie = Movie.query.get(id)
        if movie is not None:
            movie.delete()
            return jsonify({
                'success': True,
                'stetus code': 200,
                'message': f"removed movie with id = {id}"
            })
        else:
            abort(404)
        return abort(500)

    @app.route('/actors/create', methods=['GET'])
    @requires_auth('post:actor')
    def create_actor_form(jwt):
        form = ActorForm()
        return render_template('forms/new_actor.html', form=form)

    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(jwt):
        res = request.json
        print("llllllllllllllllllll", res)
        name = res['name']
        age = res['age']
        gender = res['gender']
        new_actor = Actor.query.filter(Actor.name == name).one_or_none()
        if new_actor is None:
            new_actor = Actor(name, age, gender)
            new_actor.insert()
            actors = Actor.query.all()
            actors = [actor.format() for actor in actors]
            return jsonify({
                'actors': actors,
                'success': True,
                'status code': 200
            })
        else:
            abort(409)

        return abort(500)

    @app.route('/movies/create', methods=['GET'])
    @requires_auth('post:movie')
    def create_movie_form(jwt, ):
        form = MovieForm()
        return render_template('forms/new_movie.html', form=form)

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(jwt):
        res = request.json
        title = res['title']
        release_date = res['release_date']
        new_movie = Movie.query.filter(Movie.title == title).one_or_none()
        if new_movie is None:
            new_movie = Movie(title, release_date)
            new_movie.insert()
            return jsonify({
                'success': True,
                'status code': 200,
                'movie_id': new_movie.id
            })
        else:
            abort(409)
        return abort(500)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(jwt, id):
        actor = Actor.query.get(id)
        if actor is None:
            abort(404)
        else:
            response = request.json
            for key in response:
                if key == "name":
                    actor.name = response[key]
                elif key == "age":
                    actor.age = response[key]
                else:
                    actor.gender = response[key]
            actor.update()
            return jsonify({
                'success': True,
                'status code': 200
            })
        return abort(500)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def edit_movie(jwt, id):
        movie = Movie.query.get(id)
        if movie is None:
            abort(404)
        else:
            response = request.json
            for key in response:
                if key == "title":
                    movie.title = response[key]
                else:
                    movie.release_date = response[key]
            movie.update()
            return jsonify({
                'success': True,
                'status code': 200
            })
        return abort(500)

    # handling errors
    # handling bad requests errors

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request',
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized',
        }), 401

    # handling resources not found errors

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found',
        }), 404

    # handling not allowed methods errors

    @app.errorhandler(405)
    def not_allawed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed',
        }), 405

    @app.errorhandler(409)
    def item_already_exist(error):
        return jsonify({
            'success': False,
            'error': 409,
            'message': 'item already exist',
        }), 409

    # handling unprocessable requests

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable',
        }), 422

    # handling internal server errors

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error',
        }), 500

    # @app.errorhandler(AuthError)
    # def not_found(error):
    # return jsonify({
    #   'success': False,
    #   'error': AuthError,
    #   'message': 'authentication error',
    # }), AuthError

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
