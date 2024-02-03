from typing import ClassVar

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class BookingInfo(BaseEntityModel):
    field: ClassVar[str]
