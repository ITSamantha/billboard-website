from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class CategoryFilter(Base):
    filter_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('filter.id'), nullable=False)
    category_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('category.id'), nullable=False)
