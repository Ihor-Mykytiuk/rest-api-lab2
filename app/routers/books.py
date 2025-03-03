from fastapi import APIRouter

router = APIRouter()


@router.get("/books")
async def root():
    return [{"book1": "First Book", "book2": "Second Book"}]