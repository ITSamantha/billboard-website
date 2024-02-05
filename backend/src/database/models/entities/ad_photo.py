from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class AdPhoto(AbstractBaseEntityModel):
    __tablename__ = "ad_photo"

    photo_id: Mapped[int] = mapped_column(ForeignKey("photo.id"), nullable=False)
    photo: Mapped["Photo"] = relationship(back_populates="ad_photo", uselist=False, lazy="selectin")

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_photos", uselist=False, lazy="selectin")

    is_main: Mapped[bool] = mapped_column(default=False, nullable=False)

    def __repr__(self) -> str:
        return (
            f"AdPhoto(id={self.id}, photo_id={self.photo_id}, "
            f"advertisement_id={self.advertisement_id}, is_main={self.is_main})")
