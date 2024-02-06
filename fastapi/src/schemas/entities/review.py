from typing import ClassVar
import datetime

from src.schemas.entities.base import BaseEntity, BaseEntityTime


class Review(BaseEntityTime):
    advertisement_id: ClassVar[int]
    user_id: ClassVar[int]

    text: ClassVar[str]
    rating: ClassVar[int]
