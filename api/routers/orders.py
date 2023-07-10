from fastapi import APIRouter, Response
import repository.orders as orders_repository
import schemas.orders as schemas_orders

router = APIRouter(tags=['orders'])


@router.post('/orders')
def create_a_orders(request: schemas_orders.Orders):
    return orders_repository.create_a_orders(request=request)
