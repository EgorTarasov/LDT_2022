from fastapi import APIRouter

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


@router.get("/")
async def get_places():
    return "hello"
