from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..loader import DATABASE_URL

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.sqlite"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_URL}/{POSTGRES_PROD_DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base(bind=engine)
