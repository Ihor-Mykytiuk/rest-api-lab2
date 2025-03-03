from typing import List

from fastapi import APIRouter, HTTPException
from app.models import Book, books

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_books():
    return books

@router.get("/{book_id}")
async def get_book(book_id: str):
    book = next((book for book in books if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/")
async def add_book(book: Book):
    books.append(book)
    return book

@router.delete("/{book_id}")
async def delete_book(book_id: str):
    book = next((book for book in books if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    books.remove(book)
    return {"message": "Book deleted"}
