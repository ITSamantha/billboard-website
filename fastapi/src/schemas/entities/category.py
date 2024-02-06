from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Category(BaseEntity):
    title: str
    order: int

    meta_title: str
    meta_description: str
    url: str

    parent_id: int

    bookable: bool
    map_addressable: bool
