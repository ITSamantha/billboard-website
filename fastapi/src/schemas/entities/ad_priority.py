import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdPriority(BaseEntity):
    priority_id: ClassVar[int]
    advertisement_id: ClassVar[int]

    start_time: ClassVar[datetime.datetime]
    end_time: ClassVar[datetime.datetime]
