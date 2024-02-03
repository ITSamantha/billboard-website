import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModel

MIN_BOOKING_TIME = 1
MAX_BOOKING_TIME = 168


class AdBookingAvailable(BaseEntityModel):
    __tablename__ = "ad_booking_available"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)

    time_from: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    time_end: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    min_booking_time: Mapped[ClassVar[datetime.timedelta]] = mapped_column(
        default=datetime.timedelta(hours=MIN_BOOKING_TIME))
    max_booking_time: Mapped[ClassVar[datetime.timedelta]] = mapped_column(
        default=datetime.timedelta(hours=MAX_BOOKING_TIME))

    price: Mapped[ClassVar[float]] = mapped_column(nullable=False)
