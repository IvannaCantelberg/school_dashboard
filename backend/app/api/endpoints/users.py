from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import User, UserAuth
from app.api.crud import get_users, get_user
from app.api.auth_handler import AuthJWT

router = APIRouter()


@router.get("/", response_model=dict())
def read_users(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(AuthJWT.get_current_user)):
    users = get_users(db, skip=skip, limit=limit)
    return {
        'users': users,
        'is_current_user': current_user
    }


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user
