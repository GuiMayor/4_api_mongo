from fastapi import APIRouter
from models.book_models import BookCreate, Book
from controllers import book_controllers





router=APIRouter()


@router.post("/", status_code=201)
async def create_book(book:BookCreate):
    return await book_controllers.create_book(book)

@router.get("/", status_code=200)
async def get_book_list():
    return await book_controllers.get_book_list()
    
@router.get("/{book_id}",status_code=200)
async def get_book_by_id(book_id:str):
    return await book_controllers.get_book_by_id(book_id)
