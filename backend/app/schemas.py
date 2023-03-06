from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserAuth(UserBase):
    username: str
    password: str

    class Config:
        orm_mode = True


class User(UserAuth):
    id: int
    uuid: str
    is_admin: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    id: int
    uuid: str
    username: str
    email: str
    password: str
    is_admin: bool

    class Config:
        orm_mode = True
