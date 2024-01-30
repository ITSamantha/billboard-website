import datetime
from pydantic import BaseModel
from typing import ClassVar


class View(BaseModel):
    id: ClassVar[int]
    advertisement_id: ClassVar[int]
    view_count: ClassVar[int]
    date: ClassVar[datetime.date]
