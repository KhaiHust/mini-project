import datetime

from playhouse.shortcuts import model_to_dict
from peewee import fn
from fastapi import HTTPException, status

from models.orders import Orders
from models.order_seat import Order_Seat
import schemas.orders as schemas_orders
from models.seats import Seats


def create_a_orders(request: schemas_orders.Orders):
    new_order = Orders(user_id=request.user_id,
                       calendar_id=request.calendar_id, payment=request.payment)

    new_order.save()
    # new_order = model_to_dict(new_order)
    for seat in request.seat_id:
        new_seat = Order_Seat(order_id=new_order.id, seat_id=seat)
        new_seat.save()

    return 'create a order success'


def get_orders_not_payment(user_id, payment):
    orders = Orders.select().where((Orders.user_id == user_id)
                                   & (Orders.payment == payment))

    if not orders:
        return 'No orders found', None
    orders = [model_to_dict(item) for item in orders]
    print(orders)

    for order in orders:
        seat = Order_Seat.select(Order_Seat.seat_id).where(
            Order_Seat.order_id == order.get('id'))
        total_price_query = Orders.select(fn.SUM(Seats.price).alias('price')).join(Order_Seat, on=(Order_Seat.order_id == Orders.id)).join(
            Seats, on=(Seats.id == Order_Seat.seat_id)).where(Order_Seat.order_id == order.get('id')).first()
        total_price = total_price_query.price if total_price_query else None
        seat = [item.seat_id for item in seat]
        order.update({'seat_id': seat})
        order.update({'total_price': total_price})

    return 'Get all orders not payment success', orders


def create_payment(order_id):
    order = Orders.get(Orders.id == order_id)
    order.payment = True
    order.save()
    return f'Payment order ID {order_id} success'


def delete_order(order_id):
    delete_order_seat = Order_Seat.delete().where(
        (Order_Seat.order_id == order_id)
    )
    del_order = Orders.delete().where(Orders.id == order_id)

    delete_order_seat.execute()
    del_order.execute()
    return f'Delete Order ID {order_id} success'
