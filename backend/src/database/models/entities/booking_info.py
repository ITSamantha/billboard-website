from typing import ClassVar

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import AbstractBaseEntityModel


class BookingInfo(AbstractBaseEntityModel):
    __tablename__ = "booking_info"

    field: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"BookingInfo(id={self.id}, field={self.field})"
