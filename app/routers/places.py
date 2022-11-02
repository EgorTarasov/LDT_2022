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

