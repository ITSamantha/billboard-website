from typing import Optional, List
from fastapi import Request
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base


# TODO: ADD TO ADMIN
class FilterValue(Base):
    __tablename__ = "filter_value"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    filter_id: Mapped[int] = mapped_column(ForeignKey("filter.id"), nullable=False)
    filter: Mapped["Filter"] = relationship(uselist=False, lazy="selectin")

    value: Mapped[str] = mapped_column(String(256), nullable=False)
    hint_html: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
    order: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (f"FilterValue(id={self.id}, value={self.value}, filter_id={self.filter_id},"
                f" order={self.order}, hint_html={self.hint_html})")
