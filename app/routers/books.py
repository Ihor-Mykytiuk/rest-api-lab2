from fastapi import APIRouter, HTTPException
from app.models import Book, books
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


async def get_book_by_id(book_id: str) -> Book:
    book = next((book for book in books if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/", response_model=List[Book])
async def get_books():
    return books


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: str):
    book = await get_book_by_id(book_id)
    return book


@router.post("/", status_code=201, response_model=Book)
async def add_book(book: Book):
    books.append(book)
    return book


@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str):
    book = await get_book_by_id(book_id)
    books.remove(book)
    return
