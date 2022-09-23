from fastapi import FastAPI

from routers import users

router = FastAPI()


@router.get("/")
def root_access():
    return {"message": "Hello World"}


router.include_router(users.router)
