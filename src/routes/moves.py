from flask import Blueprint, jsonify

#Models
from models.movieModel import MovieModel

main=Blueprint('movie_blueprint',__name__)

@main.route('/')    
def get_movies():
    try:
        movies = MovieModel().get_moviestest()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'menssage': "PapurroXD"}), 500