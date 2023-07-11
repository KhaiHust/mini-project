from playhouse.shortcuts import model_to_dict
from fastapi import HTTPException, status
from models.calendars import Calendars
from models.movies import Movies
import schemas.calendars as schemas_calendars
import datetime
from peewee import fn


def get_all_calendars():
    try:
        calendars = Calendars.select().order_by(Calendars.id.asc())
        calendars = [model_to_dict(calendar) for calendar in calendars]
        return calendars
    except Calendars.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Not found any calendars')


def get_all_calenders_by_date(date: datetime.date):
    calendars = Calendars.select().where(fn.DATE(Calendars.start_time) == date)
    calendars = [model_to_dict(item) for item in calendars]
    msg = f'get all calendars of {date} success' if len(
        calendars) > 0 else f'No calendar on {date}'

    return msg, calendars if len(calendars) > 0 else None


def get_all_calendars_by_movie_id(movie_id: int):
    calendars = Calendars.select().where(Calendars.movie_id == movie_id)
    msg = ''
    if not calendars:
        msg = f'No calendars of Movies ID {movie_id}'
        return msg, None
    else:
        calendars = [model_to_dict(item) for item in calendars]
        return msg, calendars


def create_calendars_movie(request: schemas_calendars.MovieCalendars):

    movie_id = int(request.movie_id)
    try:
        movie = Movies.get(Movies.id == movie_id)
    except Movies.DoesNotExist:
        return f'Not found Movie ID {movie_id}', None
    schedule = []  # luu cac lich co the nhet vao DB
    not_available = []  # luu cac lich khong the cho vao DB
    for time in request.time:
        start_time = time.start_time
        end_time = time.start_time + datetime.timedelta(minutes=movie.duration)

        avai_schedule = Calendars.select().where(((Calendars.start_time >= start_time) & (Calendars.start_time <= end_time)) | (
            (Calendars.end_time >= start_time) & (Calendars.end_time <= end_time)))
        if not avai_schedule:
            new_calendar = Calendars(
                movie_id=movie_id, start_time=start_time, end_time=end_time)

            new_calendar.save()
            schedule.append(new_calendar)
        else:
            not_available.append(start_time)

    schedule = [model_to_dict(calendar) for calendar in schedule]

    if len(schedule) == 1:
        new_schedule = schedule[0]
    msg = []
    if len(not_available) > 0:
        msg.append(f'Calendars {not_available} not valid. ')
    if len(schedule) > 0:
        msg.append(
            f'create {len(schedule)} calendars success')
    return " ".join(msg), schedule if len(schedule) > 1 else (new_schedule if len(schedule) == 1 else None)


def delete_calendar_by_id(id: int):
    try:
        calendar = Calendars.get(Calendars.id == id)
        calendar.delete_instance()
        return None
    except Calendars.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Calendar with ID {id} not found')
