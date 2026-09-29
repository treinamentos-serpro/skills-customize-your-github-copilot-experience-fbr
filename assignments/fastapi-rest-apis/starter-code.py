from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Library API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    available: bool = True


class BookCreate(BaseModel):
    title: str
    author: str


class AvailabilityUpdate(BaseModel):
    available: bool


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Kindred", author="Octavia E. Butler", available=False),
]


@app.get("/books", response_model=list[Book])
def list_books():
    """Return all books."""
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Return one book by ID."""
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    """Create a new book."""
    pass


@app.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, update: AvailabilityUpdate):
    """Update a book's availability."""
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete a book by ID."""
    pass
