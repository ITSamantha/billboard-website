import datetime

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.entities.advertisement import Advertisement, create_advertisement


class View(BaseModel):
    id: int
    # advertisement_id: int
    advertisement: Advertisement
    view_count: int
    date: datetime.date


def create_view(view: models.View) -> View:
    return View(id=view.id,
                advertisement=create_advertisement(view.advertisement) if view.advertisement else None,
                view_count=view.view_count,
                date=view.date)


class ViewCreate(BasePayload):
    advertisement_id: int
    view_count: int
    date: datetime.date
