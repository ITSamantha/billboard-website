from typing import ClassVar

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class Avatar(BaseEntityModel):
    __tablename__ = "avatar"

    photo_path: Mapped[ClassVar[str]] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[ClassVar[str]] = mapped_column(String)
