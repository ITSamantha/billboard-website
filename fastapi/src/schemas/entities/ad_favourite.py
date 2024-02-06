from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdFavourite(BaseEntity):
    advertisement_id: ClassVar[int]
    user_id: ClassVar[int]
