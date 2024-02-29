from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class AdTag(BaseModel):
    id: int
    title: str


def create_ad_tag(tag: models.AdTag) -> AdTag:
    return AdTag(id=tag.id, title=tag.title)


class AdTagUpdate(BasePayload):
    title: str


class AdTagCreate(BasePayload):
    title: str
