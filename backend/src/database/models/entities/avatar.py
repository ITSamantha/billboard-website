from typing import ClassVar

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import BaseEntityModel


class Avatar(BaseEntityModel):
    __tablename__ = "avatar"

    photo_path: Mapped[ClassVar[str]] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[ClassVar[str]] = mapped_column(String)

    user: Mapped["User"] = relationship(back_populates="avatar", uselist=False)

    def __repr__(self) -> str:
        return f"Avatar(id={self.id}, photo_path={self.photo_path})"
