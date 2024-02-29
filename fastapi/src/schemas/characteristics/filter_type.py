from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


# checkbox (multiple_select)
# text
# radio (color, select)
# numerical_interval
# date_interval

# в скобках title, отдельная строка -- functional_title

class FilterType(BaseModel):
    id: int
    title: str
    functional_title: str

    interval_placeholder_from: Optional[str]
    interval_placeholder_to: Optional[str]


def create_filter_type(filter: models.FilterType) -> FilterType:
    return FilterType(id=filter.id, title=filter.title, functional_title=filter.functional_title,
                      interval_placeholder_from=filter.interval_placeholder_from,
                      interval_placeholder_to=filter.interval_placeholder_to)


class FilterTypeCreate(BasePayload):
    title: str
    functional_title: str

    interval_placeholder_from: Optional[str] = None
    interval_placeholder_to: Optional[str] = None


class FilterTypeUpdate(BasePayload):
    title: Optional[str] = None
    functional_title: Optional[str] = None

    interval_placeholder_from: Optional[str] = None
    interval_placeholder_to: Optional[str] = None
