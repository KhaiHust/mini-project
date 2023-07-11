import datetime

from playhouse.shortcuts import model_to_dict
from peewee import fn
from fastapi import HTTPException, status
from models.movies import Movies
import schemas.movies as schemas_movies


def getAllMovies():
    try:
        movies = Movies.select().order_by(Movies.id.asc())
        movies = [model_to_dict(movie) for movie in movies]
        return movies
    except Movies.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Not found any movie')


def getMoviesById(id: int):
        movie = Movies.get_or_none(Movies.id == id)
        if not movie:
            msg = f'Movie with ID {id} not found'
            return msg, None
        movie_dict = model_to_dict(movie)
        return f'get movie Id {id} success', movie_dict



def createMovie(request: schemas_movies.Movies):
    msg = ''
    new_movie = None
    if request.start_date <= request.end_date and request.end_date >= datetime.datetime.now().date():

        new_movie = Movies(name=request.name, start_date=request.start_date,end_date=request.end_date, duration=request.duration, img=request.img, description=request.description)
        new_movie.save()
        msg = 'create movie success'
    else:
        msg = 'Date error'
    return msg, model_to_dict(new_movie) if new_movie is not None else None


def updateAMovie(id: int, request: schemas_movies.Movies):
    try:
        movie = Movies.get_by_id(id)
        movie.name = request.name
        movie.start_date = request.start_date
        movie.end_date = request.end_date
        movie.duration = request.duration
        movie.img = request.img
        movie.description = request.description
        movie.save()
        return model_to_dict(movie)
    except Movies.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Movie with ID {id} not found')


def deleteAMovieById(id: int):
    try:
        movie = Movies.get(Movies.id == id)
        movie.delete_instance()
        return None
    except Movies.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Movie with ID {id} not found')

def getMovieShowNow():
    time = datetime.datetime.now().date()
    movies = Movies.select().where((fn.DATE(Movies.start_date) <= time) & (fn.DATE(Movies.end_date) >= time))
    print(movies)
    if not movies:
        msg = f'No any movie found'
        return msg, None
    else:
        movies = [model_to_dict(item) for item in movies]
        msg = f'get movies success'
        return msg, movies
