import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.characteristics import Priority, create_priority
from src.schemas.entities.advertisement import Advertisement, create_advertisement


class AdPriority(BaseModel):
    id: int
    # priority_id: int
    priority: Priority
    # advertisement_id: int
    advertisement: Advertisement

    start_time: datetime.datetime
    end_time: datetime.datetime


def create_ad_priority(priority: models.AdPriority) -> AdPriority:
    return AdPriority(id=priority.id,
                      priority=create_priority(priority.priority) if priority.priority else None,
                      advertisement=create_advertisement(priority.advertisement) if priority.advertisement else None,
                      start_time=priority.start_time,
                      end_time=priority.end_time)


class AdPriorityUpdate(BasePayload):
    priority_id: Optional[int] = None
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None


class AdPriorityCreate(BasePayload):
    priority_id: int
    advertisement_id: int

    start_time: datetime.datetime
    end_time: datetime.datetime
