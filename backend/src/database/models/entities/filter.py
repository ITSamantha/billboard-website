from typing import ClassVar, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class Filter(BaseEntityModel):
    __tablename__ = "filter"

    title: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)

    filter_type_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("filter_type.id"), nullable=False)
    filter_type: Mapped["FilterType"] = relationship(back_populates="filters", uselist=False)

    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)

    filter_values: Mapped[List["FilterValue"]] = relationship(back_populates="filter", uselist=True)

    categories: Mapped[List["Category"]] = relationship(back_populates="filters",
                                                   uselist=True, secondary="category__filter")
    def __repr__(self) -> str:
        return f"Filter(id={self.id}, title={self.title}, filter_type_id={self.filter_type_id}, order={self.order})"
