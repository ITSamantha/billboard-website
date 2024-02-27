from typing import Optional, List

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base



class Weekday(Base):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    __tablename__ = "weekday"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    short_title: Mapped[Optional[str]] = mapped_column(String(8), unique=True)

    order: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"Weekday(id={self.id}, title={self.title}, short_title={self.short_title}, order={self.order})"
