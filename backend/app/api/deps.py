from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.db.db_setup import SessionLocal

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

