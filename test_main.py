"""This module handles the test cases for the API endpoints"""
from app import app
from fastapi.testclient import TestClient
import re

client = TestClient(app)


def test_get_books():
    """Test case for getting all the books"""
    response = client.get('/books')
    assert response.status_code == 200
    assert response.json() == {'data': [{"id": 1, "title": "The Girl With The Dragon Tattoo",
                                        "author": "Stieg Larsson", "published_year": 2005}]}


def test_get_book():
    """Test case for getting a book by passing its ID"""
    response = client.get('/books/1')
    assert response.status_code == 200
    assert response.json() == {'data': {"id": 1, "title": "The Girl With The Dragon Tattoo",
                                        "author": "Stieg Larsson", "published_year": 2005}}


def test_get_non_existent_book():
    """Test case for getting a book that does not exist"""
    response = client.get('/books/2')
    assert response.status_code == 404
    assert response.json() == {'detail': "This book does not exist"}


def test_create_book():
    """Test case for creating a book"""
    response = client.post(
        '/books', json={"title": "Gifted Hands", "author": "Ben Carson", "published_year": 1999})
    assert response.status_code == 200
    post_response = response.json()
    message = post_response["message"]
    match = re.search(r'\b\d+\b$', message)
    if match:
        book_id = int(match.group())
    assert response.json() == {
        "message": f"new book successfully added with id {book_id}"}


def test_put_book():
    """Test case for updating a book by passing its ID"""
    response = client.put('/books/1', json={"title": "The Girl With The Lower Back Tattoo",
                                            "author": "Amy Schumer", "published_year": 2005})
    assert response.status_code == 200
    assert response.json() == {
        "message": "book with id 1 is successfully updated"}


def test_put_non_existent_book():
    """Test case for updating a book that does not match the ID"""
    response = client.put('/books/2', json={"title": "The Girl With The Lower Back Tattoo",
                                            "author": "Amy Schumer", "published_year": 2005})
    assert response.status_code == 404
    assert response.json() == {"detail": "This book does not exist"}


def test_delete_book():
    """Test case for deleting a book by passing its ID"""
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert response.json() == {
        "message": "book with id 1 is successfully deleted"}


def test_delete_non_existent_book():
    """Test case for deleting a book that does not exist"""
    response = client.delete('/books/1')
    assert response.status_code == 404
    assert response.json() == {
        "detail": "This book does not exist"}
