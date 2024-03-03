import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.entities.advertisement import Advertisement, create_advertisement


class AdBookingAvailable(BaseModel):
    id: int

    # advertisement_id: int
    advertisement: Advertisement

    time_from: datetime.datetime
    time_end: datetime.datetime

    min_booking_time: Optional[datetime.datetime]
    max_booking_time: Optional[datetime.datetime]

    price: float


def create_ad_booking_available(booking: models.AdBookingAvailable) -> AdBookingAvailable:
    return AdBookingAvailable(id=booking.id, advertisement=create_advertisement(
        booking.advertisement) if booking.advertisement else None,
                              time_from=booking.time_from, time_end=booking.time_end,
                              min_booking_time=booking.min_booking_time,
                              max_booking_time=booking.max_booking_time,
                              price=booking.price
                              )


class AdBookingAvailableUpdate(BasePayload):
    id: int

    # advertisement_id: int

    time_from: Optional[datetime.datetime] = None
    time_end: Optional[datetime.datetime] = None

    min_booking_time: Optional[datetime.datetime] = None
    max_booking_time: Optional[datetime.datetime] = None

    price: Optional[float] = None


class AdBookingAvailableCreate(BasePayload):
    advertisement_id: int

    time_from: datetime.datetime
    time_end: datetime.datetime

    min_booking_time: Optional[datetime.datetime]
    max_booking_time: Optional[datetime.datetime]

    price: float
