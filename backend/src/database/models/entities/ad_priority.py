import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class AdPriority(AbstractBaseEntityModel):
    __tablename__ = "ad_priority"

    priority_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("priority.id"), nullable=False)
    priority: Mapped["Priority"] = relationship(back_populates="ad_priorities", uselist=False)

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_priorities", uselist=False)

    start_time: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    end_time: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"AdPriority(id={self.id}, priority_id={self.priority_id}, "
            f"advertisement_id={self.advertisement_id}, start_time={self.start_time}, end_time={self.end_time})")
