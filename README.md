# A Simple Book Management RESTful API

This module creates a RESTful API for managing a collection of books.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This FastAPI module provides endpoints to perform CRUD operations on a collection of books. It uses Pydantic for request and response validation.

## Features

- Retrieve all books
- Retrieve a book by ID
- Add a new book
- Update an existing book
- Delete a book by ID

## Requirements

- Python 3.7+
- FastAPI Version 0.103+
- Pydantic Version 2.5+

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/book_management_restful_api.git
```

2. Navigate to the project directory:

```bash
cd book-management-api
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the server locally, execute the following command:

```bash
uvicorn app:app --reload
```

You can then access the API at `http://localhost:8000`.

## Endpoints

- **GET /books**: Retrieves all the books.
- **GET /books/{book_id}**: Retrieves a book by its ID.
- **POST /books**: Adds a book to the collection.
- **PUT /books/{book_id}**: Updates the data of a specific book by ID.
- **DELETE /books/{book_id}**: Deletes a book by its ID.

## Models

The Pydantic model for the Book object is defined as follows:

```python
class Book(BaseModel):
    title: str
    author: str
    published_year: int
```

The `published_year` field is validated to ensure it falls within the range 1900-2100.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.