from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class BookingStatus(Base):
    PAID = 1
    NOT_PAID = 2
    IN_PROCESS = 3
    APPROVED = 4
    CANCELED = 5

    __tablename__ = "booking_status"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    def __repr__(self) -> str:
        return f"BookingStatus(id={self.id}, title={self.title})"
