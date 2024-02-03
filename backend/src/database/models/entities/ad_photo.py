from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class AdPhoto(BaseEntityModel):
    __tablename__ = "ad_photo"

    photo_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('photo.id'), nullable=False)

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)

    is_main: Mapped[ClassVar[bool]] = mapped_column(default=False, nullable=False)
