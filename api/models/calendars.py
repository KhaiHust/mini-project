from . import PeeWeeBaseModel
import peewee as p
from playhouse.postgres_ext import ArrayField
from models.movies import Movies


class Calendars(PeeWeeBaseModel):
    id = p.IntegerField(primary_key=True)
    movie_id = p.IntegerField(null = False)
    start_time = p.DateTimeField(null=False)
    end_time = p.DateTimeField(null=False)
    seat_ordered = ArrayField(p.IntegerField, default=[])
