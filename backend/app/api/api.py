from fastapi import APIRouter
from app.api.endpoints import users, auth

api_router = APIRouter()

api_router.include_router(auth.router, tags=['authentication'])
api_router.include_router(users.router, prefix="/users", tags=["users"])
