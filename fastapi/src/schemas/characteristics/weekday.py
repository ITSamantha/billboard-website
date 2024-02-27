from typing import Optional

from pydantic import BaseModel


class Weekday(BaseModel):
    id: int
    title: str
    short_title: Optional[str] = None
    order: Optional[int] = None


def create_weekday(weekday):
    return Weekday(id=weekday.id, title=weekday.title, short_title=weekday.short_title, order=weekday.order)
