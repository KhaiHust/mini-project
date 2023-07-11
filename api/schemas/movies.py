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


class Movies(BaseModel):
    id : Any
    name: str
    start_date: datetime.date
    end_date:  datetime.date
    duration: int
    img: Optional[str]
    description: str


class ShowMovies(Movies):


    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class MovieListResponse(BaseModel):
    msg: str
    data: Optional[Union[List[ShowMovies], ShowMovies]]
