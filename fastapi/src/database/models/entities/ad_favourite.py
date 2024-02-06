from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class AdFavourite(AbstractBaseEntityModel):
    __tablename__ = "ad_favourite"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_favourites", uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="ad_favourites", uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"AdFavourite(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id})")
