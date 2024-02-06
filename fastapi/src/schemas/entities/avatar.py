from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Avatar(BaseEntity):
    photo_path: str
    photo_thumb: str
