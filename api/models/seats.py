from . import PeeWeeBaseModel
import peewee as p
from playhouse.postgres_ext import ArrayField


class Seats(PeeWeeBaseModel):
    id = p.AutoField(primary_key=True)
    row = p.IntegerField(null=False)
    col = p.IntegerField(null=False)
    price = p.IntegerField(null=False)
