import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdBookingAvailable(BaseEntity):
    advertisement_id: int

    time_from: datetime.datetime
    time_end: datetime.datetime

    min_booking_time: datetime.datetime
    max_booking_time: datetime.datetime

    price: float
