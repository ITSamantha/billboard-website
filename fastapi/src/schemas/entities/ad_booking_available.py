import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdBookingAvailable(BaseEntity):
    advertisement_id: ClassVar[int]

    time_from: ClassVar[datetime.datetime]
    time_end: ClassVar[datetime.datetime]

    min_booking_time: ClassVar[datetime.datetime]
    max_booking_time: ClassVar[datetime.datetime]

    price: ClassVar[float]
