from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import User, UserAuth
from app.api.crud import get_user_by_email

router = APIRouter()


@router.post("/login", summary="Login user", response_model=User)
async def login_user(user: UserAuth, db: Session = Depends(get_db)):
    return get_user_by_email(db, email=user.email)
