from fastapi import APIRouter, Response
from typing import List
from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.calendars import Calendars
from pydantic import BaseModel
import repository.calendars as calendars_repository
import schemas.calendars as schemas_calendars

router = APIRouter(tags=['Calendars'])


@router.get('/calendars', response_model=List[schemas_calendars.Calendars])
async def get_all_calendars():
    return calendars_repository.get_all_calendars()


@router.post('/calendars', response_model=List[schemas_calendars.Calendars])
async def create_calendar_movie(request: schemas_calendars.MovieCalendars):
    return calendars_repository.create_calendars_movie(request=request)
