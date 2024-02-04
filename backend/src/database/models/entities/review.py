from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModelTime


class Review(BaseEntityModelTime):
    __tablename__ = "review"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user.id'), nullable=False)

    text: Mapped[ClassVar[str]] = mapped_column(nullable=False)
    rating: Mapped[ClassVar[int]] = mapped_column(nullable=False)
