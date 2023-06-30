
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
    try:
        movie = Movies.get(Movies.id == id)
        movie_dict = model_to_dict(movie)
        return movie_dict
    except Movies.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Movie with ID {id} not found')


def createMovie(request: schemas_movies.Movies):
    new_movie = Movies(name=request.name, start_date=request.start_date,
                       end_date=request.end_date, duration=request.duration, img=request.img, description=request.description)
    new_movie.save()
    return model_to_dict(new_movie)


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
