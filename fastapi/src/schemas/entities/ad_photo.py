from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdPhoto(BaseEntity):
    photo_id: int
    advertisement_id: int
    is_main: bool
