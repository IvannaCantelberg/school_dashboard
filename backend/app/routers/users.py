from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


class UserRegistration(BaseModel):
    name: str

@router.post("/register")
async def register_user(user: UserRegistration):
    return {"message": "User registered successfully!", "user": user.name}
