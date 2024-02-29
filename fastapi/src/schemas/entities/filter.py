from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas import FilterType, create_filter_type


class Filter(BaseModel):
    id: int
    title: str
    # filter_type_id: int
    filter_type: FilterType
    order: int


def create_filter(filter: models.Filter) -> Filter:
    return Filter(id=filter.id,
                  title=filter.title,
                  filter_type=create_filter_type(filter.filter_type) if filter.filter_type else None,
                  order=filter.order
                  )


class FilterCreate(BasePayload):
    title: str
    filter_type_id: int
    order: int


class FilterUpdate(BasePayload):
    title: Optional[str] = None
    filter_type_id: Optional[int] = None
    order: Optional[int] = None
