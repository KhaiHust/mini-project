import datetime

from playhouse.shortcuts import model_to_dict
from peewee import fn
from fastapi import HTTPException, status

from models.orders import Orders
from models.order_seat import Order_Seat
import schemas.orders as schemas_orders


def create_a_orders(request: schemas_orders.Orders):
    new_order = Orders(user_id=request.user_id,
                       calendar_id=request.calendar_id, payment=request.payment)

    new_order.save()
    # new_order = model_to_dict(new_order)
    for seat in request.seat_id:
        new_seat = Order_Seat(order_id=new_order.id, seat_id=seat)
        new_seat.save()

    return None
