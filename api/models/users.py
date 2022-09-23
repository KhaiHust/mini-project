from . import PeeWeeBaseModel
import peewee as p


class Users(PeeWeeBaseModel):
    id = p.PrimaryKeyField()
    fullname = p.TextField()
    mobile = p.TextField()
    email = p.TextField()
    activestatus = p.BooleanField()
