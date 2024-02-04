import datetime
from typing import Union, ClassVar, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import BaseEntityModelTime
from src.schemas.entities.base import BaseEntityTime


class Booking(BaseEntityModelTime):
    __tablename__ = "booking"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="bookings", uselist=False)

    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="bookings", uselist=False)

    time_from: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    time_end: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    booking_status_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("booking_status.id"),
                                                             nullable=False)
    booking_status: Mapped["BookingStatus"] = relationship(back_populates="bookings", uselist=False)

    guest_count: Mapped[Optional[ClassVar[int]]] = mapped_column()

    deadline_at: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (f"Booking(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id},"
                f"time_from={self.time_from}, time_end={self.time_end}, booking_status_id={self.booking_status_id},"
                f"guest_count={self.guest_count}, deadline_at={self.deadline_at})")

    # [{
    #   from: 12.01.2024 12:00,
    #   to: 16.01.2024 15:00
    # }, { ... }]
