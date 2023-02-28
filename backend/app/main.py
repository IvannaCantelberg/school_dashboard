from fastapi import FastAPI
from routers import users

app = FastAPI(title="Backend Api")

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/smoke")
def read_item():
    return {"data": "fake data"}

