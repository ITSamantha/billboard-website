from typing import ClassVar, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class AdTag(BaseEntityModel):
    __tablename__ = "ad_tag"

    title: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False, unique=True)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="ad_tags",
                                                                 uselist=True,
                                                                 secondary="advertisement__ad_tag")

    def __repr__(self) -> str:
        return f"AdTag(id={self.id}, title={self.title})"
