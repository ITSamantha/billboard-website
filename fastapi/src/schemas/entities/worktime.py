import datetime

from pydantic import BaseModel

from src.schemas import Weekday,  AdvertisementResponse, create_advertisement_response, create_weekday


class Worktime(BaseModel):
    id: int
    weekday_id: int
    advertisement_id: int

    start_time: datetime.time
    end_time: datetime.time


class WorktimeResponse(BaseModel):
    id: int
    weekday: Weekday
    advertisement: AdvertisementResponse
    start_time: datetime.time
    end_time: datetime.time


def create_worktime_response(worktime):
    return WorktimeResponse(id=worktime.id, weekday=create_weekday(worktime.weekday),
                            advertisement=create_advertisement_response(worktime.advertisement),
                            start_time=worktime.start_time, end_time=worktime.end_time)
