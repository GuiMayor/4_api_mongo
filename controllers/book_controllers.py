from fastapi import HTTPException
from db.mongo import book_collection
from models.book_models import Book, BookCreate
from bson import ObjectId







def book_helper(book:dict) ->Book:
    return Book(
        id=str(book["_id"]),
        title=book["title"],
        author=book['author'],
        year=book['year'],
        pages=book.get('pages'),
        
    )


async def create_book(book:BookCreate):
    try:

        new_book=book.model_dump()
        result = await  book_collection.insert_one(new_book)
        book_created = await book_collection.find_one({"_id": result.inserted_id})
        return book_helper(book_created)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Error:{str(e)}')
    

async  def get_book_list():
    try:
        books = []
        result = book_collection.find({})
        async for item in result:
            books.append(book_helper(item))
        return books
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Error:{str(e)}')
    

async def get_book_by_id(book_id:str):
    try:
        if not ObjectId.is_valid(book_id):
            raise HTTPException(status_code=400, detail="id del libro no es valido")
        book = await book_collection.find_one({'_id': ObjectId(book_id)})
        if book:
            return book_helper(book)
        return None
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Error:{str(e)}')
        