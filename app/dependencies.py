from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .sql_app import models, database

import hashlib
import uuid


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(password: str):
    return hashlib.md5(password.encode()).hexdigest()


def generate_api_token():
    return str(uuid.uuid4())

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
# e16b2ab8d12314bf4efbd6203906ea6c testuser