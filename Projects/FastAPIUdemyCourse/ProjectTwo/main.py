from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


@app.get("/health")
async def health():
    return {
        "message": "Hello!"
    }


class Book:
    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Book 1", "Author 1", "Description 1", 4),
    Book(2, "Book 2", "Author 2", "Description 2", 5),
    Book(3, "Book 3", "Author 3", "Description 3", 3),
    Book(4, "Book 4", "Author 4", "Description 4", 4),
    Book(5, "Book 5", "Author 5", "Description 5", 5),
    Book(6, "Book 6", "Author 6", "Description 6", 4),
    Book(7, "Book 7", "Author 7", "Description 7", 3),
    Book(8, "Book 8", "Author 8", "Description 8", 4),
    Book(9, "Book 9", "Author 9", "Description 9", 5),
    Book(10, "Book 10", "Author 10", "Description 10", 4)
]


class BookRequest(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A book",
                "author": "An author name",
                "description": "A book description",
                "rating": 5
            }
        }


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books(
        title: str = None,
        author: str = None,
        description: str = None,
        rating: Optional[int] = Query(None, gt=0, lt=6)
):
    result = BOOKS

    if title:
        result = list(filter(lambda book: book.title.casefold() == title.casefold(), result))
    if author:
        result = list(filter(lambda book: book.author.casefold() == author.casefold(), result))
    if description:
        result = list(filter(lambda book: book.description.casefold() == description.casefold(), result))
    if rating:
        result = list(filter(lambda book: book.rating == rating, result))

    return result


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int = Path(gt=0)):
    book = next(filter(lambda x: x.id == book_id, BOOKS), None)
    if book is None:
        return HTTPException(404, "Book was not found.")
    return book


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    BOOKS.append(new_book)


@app.put("/books", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest):
    book_to_update = next(filter(lambda book: book.id == book_request.id, BOOKS), None)
    if book_to_update is not None:
        book_to_update.title = book_request.title
        book_to_update.author = book_request.author
        book_to_update.description = book_request.description
        book_to_update.rating = book_request.rating
    else:
        return HTTPException(404, "Book was not found.")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_to_delete = next(filter(lambda book: book.id == book_id, BOOKS), None)
    if book_to_delete is not None:
        BOOKS.remove(book_to_delete)
    else:
        return HTTPException(404, "Book was not found.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
