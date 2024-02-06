import datetime
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class Worktime(BaseEntity):
    weekday_id: ClassVar[int]
    advertisement_id: ClassVar[int]

    start_time: ClassVar[datetime.time]
    end_time: ClassVar[datetime.time]
