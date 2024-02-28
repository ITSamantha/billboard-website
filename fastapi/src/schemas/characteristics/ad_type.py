from pydantic import BaseModel

from src.api.payloads.base import BasePayload


class AdType(BaseModel):
    id: int
    title: str


def create_ad_type(type):
    return AdType(id=type.id, title=type.title)


class AdTypeCreate(BasePayload):
    title: str


class AdTypeUpdate(BasePayload):
    title: str
