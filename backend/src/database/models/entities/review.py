from typing import ClassVar
import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModelTime
from src.schemas.entities.base import BaseEntity, BaseEntityTime


class Review(BaseEntityModelTime):
    __tablename__ = "review"

    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)
    user_id: ClassVar[int]

    text: ClassVar[str]
    rating: ClassVar[int]
