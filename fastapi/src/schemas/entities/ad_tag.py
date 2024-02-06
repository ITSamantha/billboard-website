from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdvertisementTag(BaseEntity):
    title: ClassVar[str]
