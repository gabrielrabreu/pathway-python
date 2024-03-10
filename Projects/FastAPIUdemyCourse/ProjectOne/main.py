from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/health")
async def health():
    return {
        "message": "Hello!"
    }

BOOKS = [
    {"id": 1, "title": "Title One", "author": "Author One", "category": "science"},
    {"id": 2, "title": "Title Two", "author": "Author Two", "category": "fiction"},
    {"id": 3, "title": "Title Three", "author": "Author Three", "category": "history"},
    {"id": 4, "title": "Title Four", "author": "Author Four", "category": "technology"},
    {"id": 5, "title": "Title Five", "author": "Author Five", "category": "fantasy"},
    {"id": 6, "title": "Title One", "author": "Author One", "category": "science"},
    {"id": 7, "title": "Title Two", "author": "Author Two", "category": "fiction"},
    {"id": 8, "title": "Title Three", "author": "Author Three", "category": "history"},
    {"id": 9, "title": "Title Four", "author": "Author Four", "category": "technology"},
    {"id": 10, "title": "Title Five", "author": "Author Five", "category": "fantasy"}
]


@app.get("/books")
async def get_books(
    title: str = None,
    author: str = None,
    category: str = None,
):
    result = BOOKS

    if title:
        result = list(filter(lambda book: book["title"].casefold() == title.casefold(), result))
    if author:
        result = list(filter(lambda book: book["author"].casefold() == author.casefold(), result))
    if category:
        result = list(filter(lambda book: book["category"].casefold() == category.casefold(), result))

    return result


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return next(filter(lambda book: book["id"] == book_id, BOOKS), None)


@app.post("/books")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books")
async def update_book(updated_book=Body()):
    book_to_update = next(filter(lambda book: book["id"] == updated_book["id"], BOOKS), None)
    if book_to_update is not None:
        book_to_update["title"] = updated_book["title"]
        book_to_update["author"] = updated_book["author"]
        book_to_update["category"] = updated_book["category"]


@app.delete("/books/{book_id}")
async def create_book(book_id: int):
    book_to_delete = next(filter(lambda book: book["id"] == book_id, BOOKS), None)
    if book_to_delete is not None:
        BOOKS.remove(book_to_delete)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
