from pydantic import BaseModel, Field
import uuid
from typing import List

class Book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    author: str
    published_year: int = Field(..., ge=1000, le=2100)


books: List[Book] = []
