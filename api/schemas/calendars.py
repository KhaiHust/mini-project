from typing import Any, List, Union, Optional
import datetime
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class Calendars(BaseModel):
    id: int
    movie_id: Any
    start_time: datetime.datetime
    end_time: datetime.datetime
    seat_ordered: Optional[list[int]]


class ShowCalendars(Calendars):
    class Config:
        orm_mode = True
        getter_dict = GetterDict


class TimeShow(BaseModel):
    start_time: datetime.datetime


class MovieCalendars(BaseModel):
    movie_id: int
    time: List[TimeShow]


class CalendersListResponse(BaseModel):

    msg: str
    data: Optional[Union[Calendars, List[Calendars]]]
