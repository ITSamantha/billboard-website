from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload


class City(BaseModel):
    id: int
    title: str


class CityUpdate(BasePayload):
    title: str


class CityCreate(BasePayload):
    title: str


def create_city(city):
    return City(id=city.id, title=city.title)
