from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class BookingInfo(BaseEntity):
    field: ClassVar[str]
