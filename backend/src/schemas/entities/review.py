from typing import ClassVar
import datetime

from src.schemas.entities.base import BaseEntity


class Review(BaseEntity):
    advertisement_id: ClassVar[int]
    user_id: ClassVar[int]

    text: ClassVar[str]
    rating: ClassVar[int]

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
