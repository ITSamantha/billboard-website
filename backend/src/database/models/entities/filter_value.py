from typing import ClassVar, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModel


class FilterValue(BaseEntityModel):
    __tablename__ = "filter_value"

    filter_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('filter.id'), nullable=False)
    value: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)
    hint_html: Mapped[Optional[ClassVar[str]]] = mapped_column(String(256))
    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)
