from . import PeeWeeBaseModel
import peewee as p


class Users(PeeWeeBaseModel):
    id = p.PrimaryKeyField()
    name = p.TextField(null=False)
    email = p.TextField(null=False)
    password = p.TextField(null=False)
    role = p.TextField(choices=['ADMIN', 'USER'])
