from pydantic import BaseModel
from typing import ClassVar


class CategoryFilter(BaseModel):
    filter_id: ClassVar[int]
    category_id: ClassVar[int]
