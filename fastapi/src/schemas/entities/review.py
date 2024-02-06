from typing import ClassVar
import datetime

from src.schemas.entities.base import BaseEntity, BaseEntityTime


class Review(BaseEntityTime):
    advertisement_id: int
    user_id: int

    text: str
    rating: int
