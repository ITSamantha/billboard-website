from fastapi import Request

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import Base


class BookingInfo(Base):
    __tablename__ = "booking_info"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    field: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"BookingInfo(id={self.id}, field={self.field})"
