import datetime
from playhouse.shortcuts import model_to_dict
from peewee import fn
from fastapi import HTTPException, status
from models.users import Users
from schemas.users import SignUpUser
def create_a_user(request : SignUpUser):
    new_user = Users(name = request.name,email = request.email, password = request.password)
    new_user.save()
    return 'create a user success', model_to_dict(new_user)