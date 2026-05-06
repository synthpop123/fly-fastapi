from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/", summary="Hello, World!")
async def read_index() -> dict[str, str]:
    return {"message": "Hello, World!"}


@router.head("/", include_in_schema=False)
async def head_index() -> None:
    return None
