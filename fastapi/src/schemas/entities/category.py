from typing import Optional

from pydantic import BaseModel

from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class Category(BaseModel):
    id: int
    title: str
    order: int

    meta_title: str
    meta_description: str
    url: str

    parent_id: int

    bookable: bool
    map_addressable: bool


class CategoryResponse(BaseModel):
    id: int
    title: str
    order: int

    meta_title: str
    meta_description: str
    url: str

    parent: Optional["CategoryResponse"] = None

    bookable: bool
    map_addressable: bool


def create_category_response(category):
    category = CategoryResponse(
        id=category.id,
        title=category.title,
        order=category.order,
        meta_title=category.meta_title,
        meta_description=category.meta_description,
        url=category.url,
        bookable=category.bookable,
        map_addressable=category.map_addressable,
        parent=create_category_response(category.parent)
    )
    return category


class CategoryShort(BaseEntity, BaseResponseSchema):
    title: str


class CategoryCreate(Category):
    pass


class CategoryUpdate(Category):
    pass
