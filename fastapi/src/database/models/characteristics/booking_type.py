from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base



class BookingType(Base):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

    __tablename__ = "booking_type"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    def __repr__(self) -> str:
        return f"BookingType(id={self.id}, title={self.title})"
