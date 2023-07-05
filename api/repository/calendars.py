import datetime
from playhouse.shortcuts import model_to_dict
from peewee import fn
from fastapi import HTTPException, status
from models.calendars import Calendars
import schemas.calendars as schemas_calendars


def get_all_calendars():
    try:
        calendars = Calendars.select().order_by(Calendars.id.asc())
        calendars = [model_to_dict(calendar) for calendar in calendars]
        return calendars
    except Calendars.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Not found any calendars')


def create_calendars_movie(request: schemas_calendars.MovieCalendars):

    movie_id = int(request.movie_id)
    schedule = []
    for time in request.time:
        # start_time_str = time.start_time.strftime("%Y-%m-%d %H:%M:%S")
        # end_time_str = time.end_time.strftime("%Y-%m-%d %H:%M:%S")
        # start_time = datetime.datetime.strptime(
        #     start_time_str, "%Y-%m-%d %H:%M:%S")
        # end_time = datetime.datetime.strptime(
        #     end_time_str, "%Y-%m-%d %H:%M:%S")

        new_calendar = Calendars(
            movie_id=movie_id, start_time=time.start_time, end_time=time.end_time)
        print(new_calendar)
        new_calendar.save()
        schedule.append(new_calendar)
    schedule = [model_to_dict(calendar) for calendar in schedule]
    return schedule


def delete_calendar_by_id(id: int):
    try:
        calendar = Calendars.get(Calendars.id == id)
        calendar.delete_instance()
        return None
    except Calendars.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Calendar with ID {id} not found')
