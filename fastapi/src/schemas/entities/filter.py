from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Filter(BaseEntity):
    title: str
    filter_type_id: int
    order: int
