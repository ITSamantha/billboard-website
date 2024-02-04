import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class AdPriority(BaseEntityModel):
    __tablename__ = "ad_priority"

    priority_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("priority.id"), nullable=False)
    priority: Mapped["Priority"] = relationship(back_populates="ad_priorities", uselist=False)

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)

    start_time: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    end_time: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
