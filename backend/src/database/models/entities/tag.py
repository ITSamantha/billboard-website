from typing import ClassVar

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class AdvertisementTag(BaseEntityModel):
    title: ClassVar[int]
