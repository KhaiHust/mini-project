from fastapi import APIRouter
import repository.calendars as calendars_repository
import schemas.calendars as schemas_calendars

router = APIRouter(tags=['Calendars'])


@router.get('/calendars', response_model=schemas_calendars.CalendersListResponse)
async def get_all_calendars():
    calendars = calendars_repository.get_all_calendars()
    return schemas_calendars.CalendersListResponse(msg='Get all calendars success', data=calendars)


@router.post('/calendars', response_model=schemas_calendars.CalendersListResponse)
async def create_calendar_movie(request: schemas_calendars.MovieCalendars):
    new_calendars = calendars_repository.create_calendars_movie(
        request=request)
    return schemas_calendars.CalendersListResponse(msg='Create calendars success', data=new_calendars)


@router.delete('/calendars/{id}', response_model=schemas_calendars.CalendersListResponse)
async def delete_calendar_by_id(id: int):
    calendars_repository.delete_calendar_by_id(id)
    return schemas_calendars.CalendersListResponse(msg=f'delete calendar {id} success', data=[])
