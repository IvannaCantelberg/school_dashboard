from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserAuth(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserAuth):
    username: str


class User(UserCreate):
    id: int
    uuid: str

    is_admin: bool

    class Config:
        orm_mode = True
