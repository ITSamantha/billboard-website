import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class View(BaseEntity):
    advertisement_id: ClassVar[int]
    view_count: ClassVar[int]
    date: ClassVar[datetime.date]
