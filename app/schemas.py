from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., ge=0, le=2100)
    summary: Optional[str] = None

    @field_validator('author')
    def author_cannot_have_numbers(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError('Author name cannot contain numbers')
        return v

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None
    summary: Optional[str] = None

# This model is used for outputting book data, including the ID
class BookOut(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
  # When creating a Pydantic model from a SQLAlchemy model, pull data from the model’s attributes, not just from a dict.
