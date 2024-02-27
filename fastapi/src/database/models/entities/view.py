import datetime
from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class View(Base):
    __tablename__ = "view"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(uselist=False, lazy="selectin")

    view_count: Mapped[int] = mapped_column(nullable=False)

    date: Mapped[datetime.date] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"View(id={self.id}, advertisement_id={self.advertisement_id}, view_count={self.view_count}, date={self.date})")
