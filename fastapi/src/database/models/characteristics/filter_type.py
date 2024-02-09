from typing import Optional, ClassVar, List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models import AbstractCharacteristicModel


class FilterType(AbstractCharacteristicModel):
    __tablename__ = "filter_type"

    functional_title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    interval_placeholder_from: Mapped[Optional[str]] = mapped_column(String(32))
    interval_placeholder_to: Mapped[Optional[str]] = mapped_column(String(32))

    filters: Mapped[List["Filter"]] = relationship(back_populates="filter_type", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"FilterType(id={self.id}, title={self.title}, functional_title={self.functional_title})"
