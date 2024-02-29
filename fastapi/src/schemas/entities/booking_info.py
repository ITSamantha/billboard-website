from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class BookingInfo(BaseModel):
    id: int
    field: str


def create_booking_info(info: models.BookingInfo) -> BookingInfo:
    return BookingInfo(id=info.id, field=info.field)


class BookingInfoCreate(BasePayload):
    field: str


class BookingInfoUpdate(BasePayload):
    field: str
