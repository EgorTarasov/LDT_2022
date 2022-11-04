from fastapi import APIRouter, Query

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
        result.append(schemas.MapItem.from_orm(i))
    return result


@router.post('/new')
def save_point(item: schemas.MapItemCreate):
    db = next(get_db())
    response = crud.create_map_item(db, item)
    return response


@router.get('/place/{item_id}')
def get_point_by_id(item_id: int):
    db = next(get_db())
    map_item = crud.get_map_item_by_id(db, item_id)
    return schemas.MapItemResponse(
        id=map_item.id,
        name=map_item.name,
        desc="desc",
        long=map_item.long,
        lat=map_item.lat
    )


@router.get("/radius")
def get_point_in_radius(lat: float, long: float, r: int):#-> list[schemas.MapItemResponse]:
    db = next(get_db())
    map_items = crud.get_map_items_in_radius(db, center_lat=lat, center_long=long, radius=r)
    response = []
    for item in map_items:
        response.append(
            schemas.MapItemResponse(
                id=item.id,
                name=item.name,
                desc="desc",
                long=item.long,
                lat=item.lat
            )
        )
    return response
