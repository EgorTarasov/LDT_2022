from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    api_token = Column(Integer, ForeignKey("tokens.id"))

    token = relationship("Token", back_populates="owner")
    # TODO: сохранение сессии
    # map_sessions = relationship("MapSession", back_populates="owner")


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    login_token = Column(String(2048))
    is_used = Column(Boolean, default=False)

    owner = relationship("User", back_populates="token")


class MapItem(Base):
    """
    types:
    - Пункты выдачи
    - Точки интереса
    """

    __tablename__ = "map_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    long = Column(Float, index=True)
    lat = Column(Float, index=True)
    type = Column(String, index=True)
    rating = Column(Float, nullable=True)


# TODO: сохранение сессии
# class MapSession(Base):
#     __tablename__ = "map_sessions"
#
#     id = Column(Integer, primary_key=True, index=True)
#     data = Column(String)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="map_session")
