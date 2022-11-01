from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from ..sql_app import models, schemas, crud
from ..dependencies import oauth2_scheme, get_db, hash_password


router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies = [Depends(get_token)],
    responses={
        404: {
            "description": "Not found",
        }
    }
)


# async def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
#     db = next(get_db())
#     print(token)
#     user = crud.get_user_by_token(db, token)
#     # if not user:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_401_UNAUTHORIZED,
#     #         detail="Invalid authentication credentials",
#     #         headers={"WWW-Authenticate": "Bearer"},
#     #     )
#     return user


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = next(get_db())

    user = crud.get_user_by_username(db, form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not user.token:
        token = crud.create_token(db, user)
    else:
        token = crud.get_token(db, user.username)
    return {"access_token": token.login_token, "token_type": "Bearer"}


def get_user(token: str = Depends(oauth2_scheme)):
    user = crud.get_user_by_token(token)
    return user


def fake_decode_token(token):
    db = next(get_db())
    user = crud.get_user_by_token(db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)

    if not user:
        exit(0)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/users/me")
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return schemas.User.from_orm(current_user)
