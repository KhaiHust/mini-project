from fastapi import APIRouter

from playhouse.shortcuts import model_to_dict
from peewee import fn

from models.users import Users
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    activestatus: bool
    fullname: str
    mobile: str
    email: str


@router.get("/api/users")
def get_all_users():
    """Get all users"""
    users = Users.select().order_by(Users.activestatus.desc(), fn.LOWER(Users.fullname))
    users = [model_to_dict(user) for user in users]
    return users


@router.post("/api/users", response_model=int)
def create_user(payload_: User):
    """Create a new user"""
    payload = payload_.dict()
    user = Users.create(**payload)
    return user.id


@router.patch("/api/users/{id}", response_model=int)
def edit_user(id: int, payload_: User):
    """Update user info"""
    payload = payload_.dict()
    user = (
        Users.update(
            activestatus=payload["activestatus"],
            fullname=payload["fullname"],
            mobile=payload["mobile"],
            email=payload["email"],
        )
        .where(Users.id == id)
        .execute()
    )
    # number of changed rows
    return user


@router.delete("/api/users/{id}")
def user_employee(id: int):
    """Delete user"""
    user = Users.get_by_id(id)
    user.delete_instance()
