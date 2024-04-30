from typing import List
from fastapi import Request

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


# TODO: ADD TO ADMIN
class Filter(Base):
    __tablename__ = "filter"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), nullable=False)

    filter_type_id: Mapped[int] = mapped_column(ForeignKey("filter_type.id"), nullable=False)
    filter_type: Mapped["FilterType"] = relationship(uselist=False, lazy="selectin")

    order: Mapped[int] = mapped_column(nullable=False)

    filter_values: Mapped[List["FilterValue"]] = relationship(uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"Filter(id={self.id}, title={self.title}, filter_type_id={self.filter_type_id}, order={self.order})"
