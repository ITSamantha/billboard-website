from typing import ClassVar

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class Photo(BaseEntityModel):
    __tablename__ = "photo"
    photo_path: ClassVar[str]
    photo_thumb: ClassVar[str]
