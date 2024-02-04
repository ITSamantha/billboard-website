from typing import ClassVar

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class Photo(BaseEntityModel):
    __tablename__ = "photo"

    photo_path: Mapped[ClassVar[str]] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[ClassVar[str]] = mapped_column(String)
