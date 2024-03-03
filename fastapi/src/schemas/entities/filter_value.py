from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.entities.filter import Filter, create_filter


class FilterValue(BaseModel):
    id: int
    # filter_id: int
    filter: Filter
    value: str
    hint_html: Optional[str] = None
    order: int


def create_filter_value(filter: models.FilterValue) -> FilterValue:
    return FilterValue(id=filter.id,
                       filter=create_filter(filter.filter) if filter.filter else None,
                       value=filter.value,
                       hint_html=filter.hint_html,
                       order=filter.order
                       )


class FilterValueCreate(BasePayload):
    filter_id: int
    value: str
    hint_html: Optional[str] = None
    order: int


class FilterValueUpdate(BasePayload):
    filter_id: Optional[int] = None
    value: Optional[str] = None
    hint_html: Optional[str] = None
    order: Optional[int] = None
