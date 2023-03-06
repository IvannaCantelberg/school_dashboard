from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate
from app.api.crud import create_user, get_user_by_email

router = APIRouter()


@router.post("/signup", summary="Create new user")
async def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
