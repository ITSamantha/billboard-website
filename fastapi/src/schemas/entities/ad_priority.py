import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class AdPriority(BaseEntity):
    priority_id: int
    advertisement_id: int

    start_time: datetime.datetime
    end_time: datetime.datetime
