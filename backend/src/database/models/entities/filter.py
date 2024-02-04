from typing import ClassVar

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class Filter(BaseEntityModel):
    __tablename__ = "filter"

    title: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)

    filter_type_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('filter_type.id'), nullable=False)
    filter_type: Mapped["FilterType"] = relationship(back_populates="filters", uselist=False)

    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)
