from . import PeeWeeBaseModel
import peewee as p


class Movies(PeeWeeBaseModel):
    id = p.IntegerField(primary_key=True)
    name = p.TextField(null=False)
    start_date = p.DateField(null=False)
    end_date = p.DateField(null=False)
    duration = p.IntegerField(null=False)
    img = p.TextField()
    description = p.TextField(null=False)
