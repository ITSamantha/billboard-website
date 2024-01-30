import datetime
from pydantic import BaseModel
from typing import ClassVar


class Worktime(BaseModel):
    id: ClassVar[int]
    weekday_id: ClassVar[int]
    advertisement_id: ClassVar[int]
    start_time: ClassVar[datetime.time]
    end_time: ClassVar[datetime.time]
