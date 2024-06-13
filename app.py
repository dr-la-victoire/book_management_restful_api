"""This module creates a RESTful API for managing a collection of books"""
from fastapi import FastAPI, HTTPException
from models import Book
from random import randint

app = FastAPI()

# the list of dictionaries for storage
# Populating the list for testing purposes
book_dict = [{"id": 1, "title": "The Girl With The Dragon Tattoo",
              "author": "Stieg Larsson", "published_year": 2005}]

# API Endpoints


@app.get('/books')
def get_books():
    """Retrieves all the books"""
    return {"data": book_dict}


@app.get('/books/{book_id}')
def get_book(book_id):
    """Retrieves a book by its ID"""
    book_id = int(book_id)
    for book in book_dict:  # checking if the ID exists
        if book_id == book["id"]:
            return {"data": book}
    raise HTTPException(status_code=404, detail="This book does not exist")


@app.post('/books')
def create_book(book: Book):
    """Adds a book data to the database"""
    books = book.dict()

    # Making sure that no 2 books have the same title, author and publishing year
    # Fixing error of books that have the same details but different IDs
    for old_book in book_dict:
        if (old_book["title"] == books["title"] and
            old_book["author"] == books["author"] and
                old_book["published_year"] == books["published_year"]):
            raise HTTPException(
                status_code=400, detail="A book with the same title, author, and published year already exists")

    # Generating a random ID (working for only 100 books in the collection)
    while True:
        # Loop will keep generating random IDs until it picks a unique ID
        book_id = randint(0, 100)
        if "id" in books:
            if not any(book_id == book["id"] for book in book_dict):
                break
        else:
            break

    # Appending to the list
    book_dict.append({"id": book_id, **book.dict()})
    return {"message": f"new book successfully added with id {book_id}"}


@app.put('/books/{book_id}')
def put_book(book_id, book: Book):
    """Updates the data of a specific book by id"""
    book_id = int(book_id)
    index = 0

    # Looking for the index in the list where the dict with the ID is located
    for the_book in book_dict:
        if book_id != the_book["id"]:
            index = index + 1  # if it's not the ID increase the index
        elif book_id == the_book["id"]:  # if the IDs match
            updated_book = book.dict()  # copy to a new dictionary
            updated_book["id"] = book_id  # make the new id the book id
            # replace the old dict with the new dict and the changes
            book_dict[index] = updated_book
            return {"message": f"book with id {book_id} is successfully updated"}
    raise HTTPException(status_code=404, detail="This book does not exist")


@app.delete('/books/{book_id}')
def delete_book(book_id):
    """Deletes a book by its ID"""
    book_id = int(book_id)  # Making sure the ID's an int
    index = 0

    # Looking for the index in the list where the dict with the ID is located
    for book in book_dict:
        if book_id != book["id"]:
            index = index + 1  # if it's not the ID increase the index
        elif book_id == book["id"]:
            book_dict.pop(index)  # if the IDs match, pop from the list
            return {"message": f"book with id {book_id} is successfully deleted"}
    raise HTTPException(status_code=404, detail="This book does not exist")
