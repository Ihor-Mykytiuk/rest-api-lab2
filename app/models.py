from pydantic import BaseModel, Field
import uuid
from typing import List
from datetime import datetime


class Book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(..., max_length=100)
    author: str = Field(..., max_length=255)
    published_year: int = Field(..., ge=1000, le=datetime.now().year)


books: List[Book] = []
