
from playhouse.shortcuts import model_to_dict
from peewee import fn

from models.movies import Movies



def getAllMovies():
    movies = Movies.select().order_by(Movies.id.asc())
    movies = [model_to_dict(movie) for movie in movies]
    return movies
