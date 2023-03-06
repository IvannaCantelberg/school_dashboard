from fastapi import APIRouter
from app.api.endponts import users, login, auth

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(auth.router, tags=["signup"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
