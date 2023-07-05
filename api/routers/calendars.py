import datetime
from fastapi import APIRouter
import repository.calendars as calendars_repository
import schemas.calendars as schemas_calendars

router = APIRouter(tags=['Calendars'])


@router.get('/calendars/all', response_model=schemas_calendars.CalendersListResponse)
async def get_all_calendars():
    calendars = calendars_repository.get_all_calendars()
    return schemas_calendars.CalendersListResponse(msg='Get all calendars success', data=calendars)


@router.get('/calendars/date/{date}', response_model=schemas_calendars.CalendersListResponse)
async def get_all_calendars_by_date(date: datetime.date = datetime.datetime.now().date()):
    msg, calendars = calendars_repository.get_all_calenders_by_date(date=date)
    return schemas_calendars.CalendersListResponse(msg=msg, data=calendars)


@router.get('/calendars/movie/{movie_id}', response_model=schemas_calendars.CalendersListResponse)
async def get_all_calendars_by_movie(movie_id: int):
    msg, calendars = calendars_repository.get_all_calendars_by_movie_id(
        movie_id=movie_id)
    return schemas_calendars.CalendersListResponse(msg=msg, data=calendars)


@router.post('/calendars', response_model=schemas_calendars.CalendersListResponse)
async def create_calendar_movie(request: schemas_calendars.MovieCalendars):
    msg, new_calendars = calendars_repository.create_calendars_movie(
        request=request)
    return schemas_calendars.CalendersListResponse(msg=msg, data=new_calendars if new_calendars is not None else None)


@router.delete('/calendars/{id}', response_model=schemas_calendars.CalendersListResponse)
async def delete_calendar_by_id(id: int):
    calendars_repository.delete_calendar_by_id(id)
    return schemas_calendars.CalendersListResponse(msg=f'delete calendar {id} success', data=[])
