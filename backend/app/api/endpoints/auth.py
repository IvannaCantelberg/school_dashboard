from fastapi import HTTPException, Depends, APIRouter, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserAuth
from app.api.crud import create_user, get_user_by_email
from app.api.auth_handler import AuthJWT

router = APIRouter()


def get_user_from_db(db: Session, email: str):
    return get_user_by_email(db, email=email)


@router.post("/signup", summary="Create new user")
async def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_from_db(db, user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"email": "Email already registered"})
    return create_user(db=db, user=user)


@router.post("/login", summary="Login user")
async def login_user(data: UserAuth, db: Session = Depends(get_db)):
    db_user = get_user_from_db(db, data.email)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = AuthJWT.create_access_token(db_user.email)

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': db_user.username
    }
