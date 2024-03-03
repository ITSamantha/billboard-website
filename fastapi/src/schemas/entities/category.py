from typing import Optional

from pydantic import BaseModel

from src.database import models


class Category(BaseModel):
    id: int
    title: str
    order: int

    meta_title: str
    meta_description: str
    url: str

    # parent: Optional["Category"] = None

    bookable: bool
    map_addressable: bool


def create_category(category: models.Category) -> Category:
    category = Category(
        id=category.id,
        title=category.title,
        order=category.order,
        meta_title=category.meta_title,
        meta_description=category.meta_description,
        url=category.url,
        bookable=category.bookable,
        map_addressable=category.map_addressable,
        parent=None  # create_category(category.parent) if category.parent else None
    )
    return category


class CategoryCreate(BaseModel):
    title: str
    order: int

    meta_title: str
    meta_description: str
    url: str

    parent_id: int

    bookable: bool
    map_addressable: bool


class CategoryUpdate(BaseModel):
    title: Optional[str] = None
    order: Optional[int] = None

    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    url: Optional[str] = None

    parent_id: Optional[int] = None

    bookable: Optional[bool] = None
    map_addressable: Optional[bool] = None
