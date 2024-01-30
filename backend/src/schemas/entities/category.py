from pydantic import BaseModel
from typing import ClassVar


class Category(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    order: ClassVar[int]
    meta_title: ClassVar[str]
    meta_description: ClassVar[str]
    url: ClassVar[str]

    parent_id: ClassVar[int]

    bookable: bool
    map_addressable: bool
