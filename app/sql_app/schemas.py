from pydantic import BaseModel
from typing import Optional


class MapItemBase(BaseModel):
    name: str
    long: float
    lat: float
    type: str
    rating: Optional[float]


class MapItemCreate(MapItemBase):
    pass


class MapItem(MapItemBase):
    id: int

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
