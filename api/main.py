from fastapi import FastAPI

from routers import movies

router = FastAPI()


# @router.get("/")
# def root_access():
#     return {"message": "Hello World"}


# router.include_router(users.router)
router.include_router(movies.router)
