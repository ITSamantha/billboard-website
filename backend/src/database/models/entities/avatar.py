from typing import ClassVar

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class Avatar(BaseEntityModel):
    photo_path: ClassVar[str]
    photo_thumb: ClassVar[str]
