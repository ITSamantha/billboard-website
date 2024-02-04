import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class Worktime(BaseEntityModel):
    __tablename__ = "worktime"

    weekday_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("weekday.id"), nullable=False)
    weekday: Mapped["Weekday"] = relationship(back_populates="worktimes", uselist=False)

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)

    start_time: Mapped[ClassVar[datetime.time]] = mapped_column(nullable=False)
    end_time: Mapped[ClassVar[datetime.time]] = mapped_column(nullable=False)
