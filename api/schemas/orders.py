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


class Orders(BaseModel):
    id: Optional[int]
    user_id: int
    calendar_id: int
    seat_id: Optional[list[int]]
    create_at: Optional[datetime.datetime]
    total_price: Optional[int]
    payment: bool


class ShowOrders(Orders):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class OrdersListResponse(BaseModel):
    msg: str
    data: Optional[Union[List[ShowOrders], ShowOrders]]