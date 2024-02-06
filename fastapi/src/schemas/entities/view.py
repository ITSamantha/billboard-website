import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class View(BaseEntity):
    advertisement_id: int
    view_count: int
    date: ClassVar[datetime.date]
