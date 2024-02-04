from typing import ClassVar

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class Filter(BaseEntityModel):
    __tablename__ = "filter"
    title: ClassVar[str]
    filter_type_id: ClassVar[int]
    order: ClassVar[int]
