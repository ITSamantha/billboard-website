from typing import ClassVar

from pydantic import BaseModel

from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class AdStatus(BaseModel):
    id: int
    title: str
    is_shown: bool


def create_ad_status(status):
    return AdStatus(id=status.id, title=status.title, is_shown=status.is_shown)


class AdStatusResponse(AdStatus, BaseResponseSchema):
    pass


class AdStatusCreate(AdStatus):
    pass


class AdStatusUpdate(AdStatus):
    pass
