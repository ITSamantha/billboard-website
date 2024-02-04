from typing import ClassVar

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModel


class BookingInfo(BaseEntityModel):
    __tablename__ = "booking_info"

    field: Mapped[ClassVar[str]] = mapped_column(nullable=False)
