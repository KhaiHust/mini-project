from . import PeeWeeBaseModel
import peewee as p
from playhouse.postgres_ext import ArrayField
class Orders(PeeWeeBaseModel):
    id = p.AutoField(primary_key=True)
    user_id = p.IntegerField(null=False)
    calendar_id = p.IntegerField(null=False)
    create_at = p.DateTimeField(null=True)
    payment = p.BooleanField(null=False)
