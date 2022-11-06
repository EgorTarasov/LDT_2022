from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

from ..dependencies import get_db
from ..sql_app import crud, schemas
# from ..dependencies import something

# TODO: add dependencies
router = APIRouter(
    prefix="/places",
    tags=["places"],
    # dependencies = [Depends(get_token)],
    responses={
        404: {
            "description": "Not found",
        }
    }
)


@router.get('/all')
def get_points(offset: int | None = Query(ge=0), count: int | None = Query(ge=1)):
    db = next(get_db())
    # FIXME
    items = crud.get_map_items(db, offset, offset+count)
    result = []
    for i in items:
        result.append(schemas.MapItemResponse.from_orm(i))
    return result


@router.get("/csv")
def get_points_csv():
    db = next(get_db())
    file = crud.get_map_items_csv(db)

    return FileResponse(file, media_type="text/csv")


@router.post('/new')
def save_point(item: schemas.MapItemCreate):
    db = next(get_db())
    response = crud.create_map_item(db, item)
    return response


@router.get('/place/{item_id}')
def get_point_by_id(item_id: int):
    db = next(get_db())
    map_item = crud.get_map_item_by_id(db, item_id)
    return schemas.MapItemResponse.from_orm(map_item)


@router.get("/radius")
def get_point_in_radius(lat: float, long: float, r: int):#-> list[schemas.MapItemResponse]:
    db = next(get_db())
    map_items = crud.get_map_items_in_radius(db, center_lat=lat, center_long=long, radius=r)
    response = []
    for item in map_items:
        response.append(schemas.MapItemResponse.from_orm(item))
    return response

