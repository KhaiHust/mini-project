from . import PeeWeeBaseModel
import peewee as p

class Order_Seat(PeeWeeBaseModel):
    id = p.IntegerField(primary_key=True)
    order_id = p.IntegerField(null=False)
    seat_id = p.IntegerField(null=False)

