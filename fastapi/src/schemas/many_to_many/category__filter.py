from pydantic import BaseModel
from typing import ClassVar


class CategoryFilter(BaseModel):
    filter_id: int
    category_id: int
