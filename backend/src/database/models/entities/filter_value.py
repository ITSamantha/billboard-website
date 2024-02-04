from typing import ClassVar, Optional, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import BaseEntityModel


class FilterValue(BaseEntityModel):
    __tablename__ = "filter_value"

    filter_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("filter.id"), nullable=False)
    filter: Mapped["Filter"] = relationship(back_populates="filter_values", uselist=False)

    value: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)
    hint_html: Mapped[Optional[ClassVar[str]]] = mapped_column(String(256))
    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="filter_values",
                                                                 uselist=True, secondary="advertisement__filter_value")

    def __repr__(self) -> str:
        return (f"FilterValue(id={self.id}, value={self.value}, filter_id={self.filter_id},"
                f" order={self.order}, hint_html={self.hint_html})")
