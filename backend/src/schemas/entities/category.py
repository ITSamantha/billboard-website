from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Category(BaseEntity):
    title: ClassVar[str]
    order: ClassVar[int]

    meta_title: ClassVar[str]
    meta_description: ClassVar[str]
    url: ClassVar[str]

    parent_id: ClassVar[int]

    bookable: ClassVar[bool]
    map_addressable: ClassVar[bool]
