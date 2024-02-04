from typing import List

from sqlalchemy.orm import relationship, Mapped

from src.database.models.characteristics.base import AbstractCharacteristicModel


class BookingStatus(AbstractCharacteristicModel):
    __tablename__ = "booking_status"

    bookings: Mapped[List["Booking"]] = relationship(back_populates="booking_status", uselist=True)

    def __repr__(self) -> str:
        return f"BookingStatus(id={self.id}, title={self.title})"
