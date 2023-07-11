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

class Users(BaseModel):
    id  : int
    name : str
    email : str
    password : str
    role : str

class SignUpUser(BaseModel):
    name : str
    email : str
    password : str


