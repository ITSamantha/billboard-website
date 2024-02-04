from typing import ClassVar, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModel


class Category(BaseEntityModel):
    __tablename__ = "category"

    title: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)

    meta_title: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    meta_description: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    url: Mapped[ClassVar[str]] = mapped_column(nullable=False)

    parent_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey('category.id'))

    bookable: Mapped[ClassVar[bool]] = mapped_column(nullable=False, default=False)
    map_addressable: Mapped[ClassVar[bool]] = mapped_column(nullable=False, default=False)
