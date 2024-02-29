import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas import Weekday, create_weekday, Advertisement, create_advertisement


class Worktime(BaseModel):
    id: int
    # weekday_id: int
    weekday: Weekday
    # advertisement_id: int
    advertisement: Advertisement

    start_time: datetime.time
    end_time: datetime.time


def create_worktime(worktime):
    return Worktime(id=worktime.id,
                    weekday=create_weekday(worktime.weekday) if worktime.weekday else None,
                    advertisement=create_advertisement(worktime.advertisement) if worktime.advertisement else None,
                    start_time=worktime.start_time,
                    end_time=worktime.end_time)


class WorktimeCreate(BasePayload):
    weekday_id: int
    advertisement_id: int

    start_time: datetime.time
    end_time: datetime.time


class WorktimeUpdate(BasePayload):
    weekday_id: Optional[int] = None
    start_time: Optional[datetime.time] = None
    end_time: Optional[datetime.time] = None
