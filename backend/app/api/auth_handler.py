import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.api.crud import get_user_by_email
from app.api.deps import get_db

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")
auth_schema = HTTPBearer()

os.environ['JWT_SECRET_KEY'] = "7fc535d83027d787134f996f13013b0d0d6ada083727a84c"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']


class AuthJWT:

    @staticmethod
    def create_access_token(user_identity: str, expires_delta: Optional[timedelta] = None):
        payload = {
            "user_identity": user_identity
        }
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        payload.update({"exp": expire})
        encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def get_current_user(credential: HTTPAuthorizationCredentials = Security(auth_schema), db: Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(credential.credentials, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("user_identity")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = get_user_by_email(db, email=email)
        if user is None:
            raise credentials_exception
        return user
