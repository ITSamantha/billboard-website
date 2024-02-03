from typing import Optional, ClassVar

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import AbstractModel


class FilterType(AbstractModel):
    __tablename__ = "filter_type"

    functional_title: Mapped[ClassVar[str]] = mapped_column(String(256), unique=True, nullable=False, index=True),

    interval_placeholder_from: Mapped[Optional[ClassVar[str]]] = mapped_column(String(32))
    interval_placeholder_to: Mapped[Optional[ClassVar[str]]] = mapped_column(String(32))
