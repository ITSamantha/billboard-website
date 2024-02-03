from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel


class AdFavourite(BaseEntityModel):
    __tablename__ = "ad_favourite"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user.id'), nullable=False)
