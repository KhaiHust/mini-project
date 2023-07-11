from fastapi import APIRouter

from playhouse.shortcuts import model_to_dict
from peewee import fn

# from ..models.users import Users

from schemas.users import SignUpUser
import repository.users as user_repository
from pydantic import BaseModel

router = APIRouter(tags=['users'])

@router.post('/users')
def create_a_user(request : SignUpUser):
    return user_repository.create_a_user(request)









