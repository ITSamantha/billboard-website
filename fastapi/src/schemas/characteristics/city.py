from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class City(BaseModel):
    id: int
    title: str


class CityResponse(BaseModel):
    id: int
    title: str


class CityUpdate(BasePayload):
    title: Optional[str] = None


def create_city_response(city):
    return CityResponse(id=city.id, title=city.title)
