import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class View(BaseEntityModel):
    __tablename__ = "view"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    view_count: Mapped[ClassVar[int]] = mapped_column(nullable=False)
    date: Mapped[ClassVar[datetime.date]] = mapped_column(nullable=False)
