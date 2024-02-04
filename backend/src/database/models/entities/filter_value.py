from typing import ClassVar, Union, Optional

from src.database.models.entities.base import BaseEntityModel


class FilterValue(BaseEntityModel):
    __tablename__ = "filter_value"

    filter_id: ClassVar[int]
    value: ClassVar[str]
    hint_html: Optional[ClassVar[str]]
    order: ClassVar[int]
