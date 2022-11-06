from typing import Any

from pydantic import BaseModel, confloat, constr, Json
from typing import Optional


class MapItemBase(BaseModel):
    name: constr(min_length=3, max_length=256)
    abbrev_ao: str
    address: str
    rating: Optional[confloat(ge=0.0, le=5.0)]
    type: str
    desc: constr(max_length=256)
    long: confloat(ge=-180.0, le=180)
    lat: confloat(ge=-90, le=90)


class MapItemCreate(MapItemBase):
    pass


class MapItemResponse(MapItemBase):
    id: int

    class Config:
        orm_mode=True



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
