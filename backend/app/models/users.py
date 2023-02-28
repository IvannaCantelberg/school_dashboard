from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    surname: str
    email: str
    password: str