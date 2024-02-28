from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class BookingStatus(BaseModel):
    id: int
    title: str


def create_booking_status(status: models.BookingStatus) -> BookingStatus:
    return BookingStatus(id=status.id, title=status.title)


class BookingStatusCreate(BasePayload):
    title: str


class BookingStatusUpdate(BasePayload):
    title: str
