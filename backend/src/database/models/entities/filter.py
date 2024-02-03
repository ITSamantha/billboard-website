from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Filter(BaseEntityModel):
    title: ClassVar[str]
    filter_type_id: ClassVar[int]
    order: ClassVar[int]
