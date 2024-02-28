from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class AdStatus(BaseModel):
    id: int
    title: str
    is_shown: bool


def create_ad_status(status: models.AdStatus) -> AdStatus:
    return AdStatus(id=status.id, title=status.title, is_shown=status.is_shown)


class AdStatusCreate(BasePayload):
    title: str
    is_shown: bool


class AdStatusUpdate(BasePayload):
    title: Optional[str] = None
    is_shown: Optional[bool] = None
