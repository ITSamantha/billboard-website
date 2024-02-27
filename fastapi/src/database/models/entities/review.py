import datetime
from typing import Optional

from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base


class Review(Base):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")

    text: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now(),
                                                          onupdate=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (f"Review(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id},"
                f"text={self.text}, rating={self.rating})")
