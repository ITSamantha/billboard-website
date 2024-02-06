from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdFavourite(BaseEntity):
    advertisement_id: int
    user_id: int
