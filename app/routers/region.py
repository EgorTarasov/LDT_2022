from fastapi import APIRouter, Query

from ..dependencies import get_db
from ..sql_app import crud, schemas
# from ..dependencies import something

# TODO: add dependencies
router = APIRouter(
    prefix="/region",
    tags=["region"],
    # dependencies = [Depends(get_token)],
    responses={
        404: {
            "description": "Not found",
        }
    }
)


@router.post('/new')
def create_region(item: schemas.RegionBase):
    db = next(get_db())
    item = crud.create_region(db, item)
    return schemas.Region.from_orm(item)


@router.get('/all')
def get_regions_all() -> list[schemas.Region]:
    db = next(get_db())
    items = crud.get_region_all(db)    
    result = []
    for i in items:
        result.append(schemas.Region.from_orm(i))
    return result
