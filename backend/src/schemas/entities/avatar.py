from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Photo(BaseEntity):
    photo_path: ClassVar[str]
    photo_thumb: ClassVar[str]
