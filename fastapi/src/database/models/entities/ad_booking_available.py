import datetime
from typing import Optional

from fastapi import Request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base

MIN_BOOKING_TIME = 1
MAX_BOOKING_TIME = 168


class AdBookingAvailable(Base):
    __tablename__ = "ad_booking_available"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(uselist=False,
                                                          lazy="selectin")

    time_from: Mapped[datetime.datetime] = mapped_column(nullable=False)
    time_end: Mapped[datetime.datetime] = mapped_column(nullable=False)

    min_booking_time: Mapped[datetime.timedelta] = mapped_column(
        default=datetime.timedelta(hours=MIN_BOOKING_TIME))
    max_booking_time: Mapped[datetime.timedelta] = mapped_column(
        default=datetime.timedelta(hours=MAX_BOOKING_TIME))

    price: Mapped[float] = mapped_column(nullable=False)

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (
            f"AdBookingAvailable(id={self.id}, advertisement_id={self.advertisement_id}, time_from={self.time_from},"
            f" time_end={self.time_end}, price={self.price})")
