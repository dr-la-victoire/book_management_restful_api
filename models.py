"""This module implements the Pydantic models for request and response validation"""
from pydantic import BaseModel, validator


class Book(BaseModel):
    """This class describes the Pydantic model"""
    title: str
    author: str
    published_year: int

    # Making sure published_year is a valid year
    @validator('published_year')
    def validate_year(cls, year):
        """This function ensures the year is a valid year"""
        if year < 1900 or year > 2100:
            raise ValueError("Published year must be between 1900 and 2100")
        return year
