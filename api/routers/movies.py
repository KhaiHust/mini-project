from fastapi import APIRouter, Response
from typing import List
from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.movies import Movies
from pydantic import BaseModel
import repository.movies as movies_repository
import schemas.movies as schemas_movies

router = APIRouter(tags=['Movies'])


@router.get('/movies', response_model=schemas_movies.MovieListResponse)
async def get_all_movies():
    movies = movies_repository.getAllMovies()
    return schemas_movies.MovieListResponse(msg='get all movies success', data=movies)


@router.get('/movies/{id}', response_model=schemas_movies.MovieListResponse)
async def get_movie_by_id(id: int):
    movie = movies_repository.getMoviesById(id)
    return schemas_movies.MovieListResponse(msg=f'get movie {id} success', data=[movie])


@router.post('/movies', response_model=schemas_movies.MovieListResponse)
async def create_a_movie(request: schemas_movies.Movies):
    movie = movies_repository.createMovie(request)
    return schemas_movies.MovieListResponse(msg='create a movie success', data=[movie])


@router.put('/movies/{id}', response_model=schemas_movies.MovieListResponse)
async def update_a_movie(id, request: schemas_movies.Movies):
    movie = movies_repository.updateAMovie(id, request)
    return schemas_movies.MovieListResponse(msg=f'update movie {id} success', data=[movie])


@router.delete('/movies/{id}', response_model=schemas_movies.MovieListResponse)
async def delete_a_movie(id: int):
    movies_repository.deleteAMovieById(id=id)
    return schemas_movies.MovieListResponse(msg=f'delete movie {id} success', data=[])
