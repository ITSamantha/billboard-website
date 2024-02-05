import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class View(AbstractBaseEntityModel):
    __tablename__ = "view"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="views", uselist=False)

    view_count: Mapped[ClassVar[int]] = mapped_column(nullable=False)

    date: Mapped[ClassVar[datetime.date]] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"View(id={self.id}, advertisement_id={self.advertisement_id}, view_count={self.view_count}, date={self.date})")
