from fastapi import APIRouter, Response
import repository.orders as orders_repository
import schemas.orders as schemas_orders

router = APIRouter(tags=['orders'])


@router.post('/orders', response_model=schemas_orders.OrdersListResponse)
def create_a_orders(request: schemas_orders.Orders):
    msg = orders_repository.create_a_orders(request=request)
    return schemas_orders.OrdersListResponse(msg=msg, data=None)


@router.get('/orders/user_id={user_id}/payment={payment}', response_model=schemas_orders.OrdersListResponse)
def get_all_orders_not_payment(user_id: int, payment: bool):
    msg, orders = orders_repository.get_orders_not_payment(user_id, payment)
    return schemas_orders.OrdersListResponse(msg=msg, data=orders)


@router.patch('/orders/payment/{order_id}', response_model=schemas_orders.OrdersListResponse)
def update_payment(order_id: int):
    msg = orders_repository.create_payment(order_id=order_id)
    return schemas_orders.OrdersListResponse(msg=msg, data=None)


@router.delete('/orders/{order_id}', response_model=schemas_orders.OrdersListResponse)
def delete_order_by_id(order_id: int):
    msg = orders_repository.delete_order(order_id=order_id)
    return schemas_orders.OrdersListResponse(msg=msg, data=None)
