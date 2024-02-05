import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class Worktime(AbstractBaseEntityModel):
    __tablename__ = "worktime"

    weekday_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("weekday.id"), nullable=False)
    weekday: Mapped["Weekday"] = relationship(back_populates="worktimes", uselist=False)

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="worktimes", uselist=False)

    start_time: Mapped[ClassVar[datetime.time]] = mapped_column(nullable=False)
    end_time: Mapped[ClassVar[datetime.time]] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"Worktime(id={self.id}, advertisement_id={self.advertisement_id}, weekday_id={self.weekday_id}, start_time={self.start_time}, end_time={self.end_time})")
