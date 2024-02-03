from typing import ClassVar, Union

from src.schemas.entities.base import BaseEntity


class FilterValue(BaseEntityModel):
    filter_id: ClassVar[int]
    value: ClassVar[str]
    hint_html: Union[ClassVar[str], None]
    order: ClassVar[int]
