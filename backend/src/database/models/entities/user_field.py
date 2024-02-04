from typing import ClassVar

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModel


class UserField(BaseEntityModel):
    __tablename__ = "user_field"

    type: Mapped[ClassVar[str]] = mapped_column(String(128), nullable=False)
    title: Mapped[ClassVar[str]] = mapped_column(String(128), nullable=False)
    order: Mapped[ClassVar[int]] = mapped_column(nullable=False)
