from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from .dependencies import get_query_token, get_token_header
from .sql_app import models, database
from .routers import users, places, token

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
)

app.include_router(places.router)
app.include_router(users.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}
