from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


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
