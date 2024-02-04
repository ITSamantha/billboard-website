from typing import ClassVar

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class AdTag(BaseEntityModel):
    __tablename__ = "ad_tag"

    title: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False, unique=True)
