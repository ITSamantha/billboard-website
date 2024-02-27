from typing import Optional, List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base



class FilterType(Base):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

    __tablename__ = "filter_type"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    functional_title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    interval_placeholder_from: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    interval_placeholder_to: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)

    filters: Mapped[List["Filter"]] = relationship(back_populates="filter_type", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"FilterType(id={self.id}, title={self.title}, functional_title={self.functional_title})"
