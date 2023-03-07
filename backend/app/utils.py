from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

os.environ['JWT_SECRET_KEY'] = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']


class Hash:
    @staticmethod
    def bcrypt(plain_password: str) -> str:
        return password_context.hash(plain_password)

    @staticmethod
    def verify(plain_password: str, hashed_pass: str) -> bool:
        return password_context.verify(plain_password, hashed_pass)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
