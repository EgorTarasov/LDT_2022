# CRUD - Create Read Update Delete
from sqlalchemy.orm import Session

from . import models, schemas
from ..dependencies import hash_password, generate_api_token


# User
def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_token(db: Session, token: str) -> models.User:
    db_token = db.query(models.Token).filter(models.Token.login_token == token).first()
    return db.query(models.User).filter(models.User.api_token == db_token.id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Token
def create_token(db: Session, user: models.User):
    token = models.Token(
        login_token=generate_api_token(),
        is_used=True
    )
    db.add(token)
    db.commit()
    user.token = token
    db.commit()
    db.refresh(token)
    db.refresh(user)
    return token


def get_token(db: Session, username: str) -> models.Token:
    return db.query(models.User).filter(models.User.username == username).first().token


# MapItems
def get_map_items(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.MapItem).offset(offset).limit(limit).all()[offset:(offset + limit)]


def create_map_item(db: Session, item: schemas.MapItemCreate):
    db_item = models.MapItem(
            name=item.name,
            long=item.long,
            lat=item.lat,
            type=item.type,
            rating=item.rating
        )
    db.add(db_item)
    db.commit()
    db.flush()
    return schemas.MapItem.from_orm(db_item)



