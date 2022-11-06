# CRUD - Create Read Update Delete
import csv
import os

from sqlalchemy.orm import Session
from sqlalchemy import func

#FIXME: apt install geos
# from shapely.geometry import Point
# from shapely.geometry.polygon import Polygon

import math

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
def get_map_items(db: Session, offset: int = 0, limit: int = 100) -> list[models.MapItem]:
    return db.query(models.MapItem).offset(offset).limit(limit).all()[offset:(offset + limit)]


def get_map_items_csv(db: Session):
    items = db.query(models.MapItem).all()
    print(os.getcwd())
    print(os.listdir())
    with open("files/data.csv", "w+", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "type", "rating", "abbrev_ao", "long", "lat", "desc"])
        for i in items:
            writer.writerow([i.id, i.name, i.type, i.rating, i.abbrev_ao, i.long, i.lat, i.desc])

    return "files/data.csv"


def get_map_items_in_radius(db: Session, center_lat: float, center_long: float, radius: int) -> list[models.MapItem]:
    # https://rodionoff.space/all/points-in-radius/
    # -- квадрат
    # (LAT < 55.769367216557 AND LAT > 55.733380783443)
    # AND
    # (LON < 37.648729735553 AND LON > 37.584786264447)
    # AND
    # -- Пифагор
    # POW((LAT - 55.751374) * 111153, 2) + POW((LON - 37.616758) * 62555.252801631, 2) < 4000000
    k1 = math.pi / 180 / 2
    k2 = math.pi / 180
    c1 = 6371000 * 2
    # (c1 * math.asin(math.sqrt(
    #     math.pow(
    #         math.sin(models.MapItem.lat - math.fabs(center_lat)
    #                  * k), 2)
    #     + math.cos(
    #         models.MapItem.lat * k2) * math.cos(math.fabs(center_lat) * k2) * math.sin(
    #         (models.MapItem.long - center_long) * k) ** 2))) < radius
    center_long, center_lat = math.fabs(center_long), math.fabs(center_lat)
    return db.query(models.MapItem).where(
        (c1 * func.asin(
            func.sqrt(
                func.power(
                    func.sin((models.MapItem.lat - center_lat) * k1),
                    2
                ) + func.cos(models.MapItem.lat * k2) * func.cos(center_lat * k2) *
                func.power(
                    func.sin((models.MapItem.long - center_long) * k1),
                    2
                )
            )
        )
         ) < radius
    ).all()


def get_map_item_by_id(db: Session, item_id: int) -> models.MapItem:
    return db.query(models.MapItem).filter(models.MapItem.id == item_id).one_or_none()


def create_map_item(db: Session, item: schemas.MapItemCreate) -> schemas.MapItemResponse:
    # db_regions = db.query(models.Region).all()
    # regions_shapes = []
    # abbrev_ao = False
    # for region in db_regions:
    #     coordinates = []
    #     for polygon in region.geometry["coordinates"]:
    #         coordinates.append(polygon)
    #     polygons = [Polygon(points) for points in coordinates]
    #     point = Point(item.long, item.lat)
    #     for p in polygons:
    #         if p.contains(point):
    #             abbrev_ao = region.abbrev_ao
    #     if abbrev_ao:
    #         break

    db_item = models.MapItem(
        name=item.name,
        abbrev_ao=item.abbrev_ao,
        address=item.address,
        desc=item.desc,
        long=item.long,
        lat=item.lat,
        type=item.type,
        rating=item.rating
    )
    db.add(db_item)
    db.flush()
    return schemas.MapItemResponse.from_orm(db_item)


# Regions
def create_region(db: Session, item: schemas.RegionBase) -> schemas.Region:
    db_item = models.Region(**item.dict())
    db.add(db_item)
    db.flush()
    return db_item


def get_region_all(db: Session) -> list[models.Region]:
    return db.query(models.Region).all()


def get_points_in_region(db: Session) -> list[models.MapItem] | None:

    return None
