import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModel

MIN_BOOKING_TIME = 1
MAX_BOOKING_TIME = 168


class AdBookingAvailable(AbstractBaseEntityModel):
    __tablename__ = "ad_booking_available"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_bookings_available", uselist=False)

    time_from: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    time_end: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    min_booking_time: Mapped[ClassVar[datetime.timedelta]] = mapped_column(
        default=datetime.timedelta(hours=MIN_BOOKING_TIME))
    max_booking_time: Mapped[ClassVar[datetime.timedelta]] = mapped_column(
        default=datetime.timedelta(hours=MAX_BOOKING_TIME))

    price: Mapped[ClassVar[float]] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"AdBookingAvailable(id={self.id}, advertisement_id={self.advertisement_id}, time_from={self.time_from},"
            f" time_end={self.time_end}, price={self.price})")
