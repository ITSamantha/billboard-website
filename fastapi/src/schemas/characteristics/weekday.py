from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload


class Weekday(BaseModel):
    id: int
    title: str
    short_title: Optional[str] = None
    order: Optional[int] = None


def create_weekday(weekday):
    return Weekday(id=weekday.id, title=weekday.title, short_title=weekday.short_title, order=weekday.order)


class WeekdayUpdate(BasePayload):
    title: Optional[str] = None
    short_title: Optional[str] = None
    order: Optional[int] = None
