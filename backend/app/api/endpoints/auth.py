from fastapi import HTTPException, Depends, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate
from app.api.crud import create_user, get_user_by_username, get_user_by_email
from app.utils import create_access_token

router = APIRouter()


@router.post("/signup", summary="Create new user")
async def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return create_user(db=db, user=user)


@router.post("/login", summary="Login user")
async def login_user(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = create_access_token({'sub': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': user.username
    }
