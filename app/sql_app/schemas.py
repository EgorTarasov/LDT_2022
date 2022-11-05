from typing import Any

from pydantic import BaseModel, confloat, constr, Json
from typing import Optional


class MapItemBase(BaseModel):
    name: constr(min_length=3, max_length=256)
    long: confloat(ge=-180.0, le=180)
    lat: confloat(ge=-90, le=90)
    type: constr(min_length=3, max_length=30)
    rating: Optional[confloat(ge=0.0, le=5.0)]


class MapItemCreate(MapItemBase):
    pass


class MapItemResponse(BaseModel):
    id: int
    name: constr(min_length=3, max_length=256)
    desc: constr(max_length=256)
    long: confloat(ge=-180.0, le=180)
    lat: confloat(ge=-90, le=90)


class MapItem(MapItemBase):
    id: int
    abbrev_ao: str
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class Geometry(BaseModel):
    type: str
    coordinates: list[list[list[float, float]]]


class RegionBase(BaseModel):
    name: str
    name_ao: str
    okato: int
    abbrev_ao: str
    geometry: Geometry

class Region(RegionBase):
    id: int

    class Config:
        orm_mode = True