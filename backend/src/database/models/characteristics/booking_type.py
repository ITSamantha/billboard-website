from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class BookingType(AbstractCharacteristicModel):
    __tablename__ = "booking_type"

    # TODO: Найти, где использовали. Дописать relationship
    # bookings: Mapped[List["Booking"]] = relationship(back_populates="booking_type", uselist=True)

    def __repr__(self) -> str:
        return f"BookingType(id={self.id}, title={self.title})"
