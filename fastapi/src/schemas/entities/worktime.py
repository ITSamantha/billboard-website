import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Worktime(BaseEntity):
    weekday_id: int
    advertisement_id: int

    start_time: datetime.time
    end_time: datetime.time
