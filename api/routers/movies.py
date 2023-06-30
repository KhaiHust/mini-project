from fastapi import APIRouter

from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.movies import Movies
from pydantic import BaseModel
import repository.movies as Movies
router = APIRouter()


@router.get('/movies')
def get_all_movies():
    return Movies.getAllMovies()
