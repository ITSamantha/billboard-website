from typing import ClassVar, Union

from src.schemas.entities.base import BaseEntity


class FilterValue(BaseEntity):
    filter_id: int
    value: str
    hint_html: Union[str, None]
    order: int
