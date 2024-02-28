from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class BookingType(BaseModel):
    id: int
    title: str


def create_booking_type(type: models.BookingType) -> BookingType:
    return BookingType(id=type.id, title=type.title)


class BookingTypeCreate(BasePayload):
    title: str


class BookingTypeUpdate(BasePayload):
    title: str
