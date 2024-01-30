import datetime
from pydantic import BaseModel
from typing import ClassVar


class AdPriority(BaseModel):
    id: ClassVar[int]
    priority_id: ClassVar[int]
    advertisement_id: ClassVar[int]
    start_time: ClassVar[datetime.datetime]
    end_time: ClassVar[datetime.datetime]
