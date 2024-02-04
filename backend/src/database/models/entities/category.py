from typing import ClassVar, Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import BaseEntityModel


class Category(BaseEntityModel):
    __tablename__ = "category"

    title: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)

    meta_title: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    meta_description: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    url: Mapped[ClassVar[str]] = mapped_column(nullable=False)

    parent_id: Mapped[Optional[ClassVar[int]]] = mapped_column(ForeignKey("category.id"))
    parent: Mapped["Category"] = relationship()

    bookable: Mapped[ClassVar[bool]] = mapped_column(nullable=False, default=False)
    map_addressable: Mapped[ClassVar[bool]] = mapped_column(nullable=False, default=False)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="categories",
                                                                 uselist=True,
                                                                 secondary="advertisement__category")
    filters: Mapped[List["Filter"]] = relationship(back_populates="categories",
                                                   uselist=True, secondary="category__filter")

    def __repr__(self) -> str:
        return (f"Category(id={self.id}, title={self.title}, order={self.order}, meta_title={self.meta_title},"
                f"meta_description={self.meta_description}, url={self.url}, parent_id={self.parent_id},"
                f"bookable={self.bookable}, map_addressable={self.map_addressable})")
