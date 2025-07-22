from fastapi import HTTPException
from db.mongo import book_collection
from models.book_models import Book, BookCreate





def book_helper(book:dict) ->Book:
    return Book(
        id=str(book["_id"]),
        title=book("title"),
        author=book('author'),
        year=book('year'),
        pages=book.get('pages'),
        
    )
async def create_book(book:BookCreate):
    try:
        new_book=book.model_dump()
        result = await book_collection.insert_one(new_book)
        