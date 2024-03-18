from typing import Optional, List
from fastapi import Request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, joinedload, selectinload

from src.database.models.base import Base


# TODO: ADD TO ADMIN
class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(nullable=False)
    order: Mapped[int] = mapped_column(nullable=False)

    meta_title: Mapped[str] = mapped_column(nullable=False)
    meta_description: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)

    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("category.id"))
    parent: Mapped["Category"] = relationship(lazy='subquery', uselist=False)

    children: Mapped[List["Category"]] = relationship("Category", cascade='all, delete-orphan')

    bookable: Mapped[bool] = mapped_column(nullable=False, default=False)
    map_addressable: Mapped[bool] = mapped_column(nullable=False, default=False)

    def __repr__(self) -> str:
        return (f"Category(id={self.id}, title={self.title}, order={self.order}, meta_title={self.meta_title},"
                f"meta_description={self.meta_description}, url={self.url}, parent_id={self.parent_id},"
                f"bookable={self.bookable}, map_addressable={self.map_addressable})")
