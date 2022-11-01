from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header
from .sql_app import models, database
from .routers import users, places, token

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    #dependencies=[Depends(get_query_token)]
)


app.include_router(users.router)
app.include_router(places.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
