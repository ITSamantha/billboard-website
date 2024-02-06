from typing import ClassVar, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class Photo(AbstractBaseEntityModel):
    __tablename__ = "photo"

    photo_path: Mapped[str] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[str] = mapped_column(String)

    ad_photo: Mapped[List["AdPhoto"]] = relationship(back_populates="photo", uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return f"Photo(id={self.id}, photo_path={self.photo_path})"
