from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class AdFavourite(BaseEntityModel):
    __tablename__ = "ad_favourite"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_favourites", uselist=False)

    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="ad_favourites", uselist=False)

    def __repr__(self) -> str:
        return (
            f"AdFavourite(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id})")
