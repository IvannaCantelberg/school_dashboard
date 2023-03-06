import uvicorn
from fastapi import FastAPI

from app.api.api import api_router
from db.db_setup import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
