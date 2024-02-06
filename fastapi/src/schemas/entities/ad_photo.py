from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdPhoto(BaseEntity):
    photo_id: ClassVar[int]
    advertisement_id: ClassVar[int]
    is_main: ClassVar[bool]
