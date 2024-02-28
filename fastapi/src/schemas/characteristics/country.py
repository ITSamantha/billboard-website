from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload


class Country(BaseModel):
    id: int
    title: str


class CountryResponse(BaseModel):
    id: int
    title: str


class CountryUpdate(BasePayload):
    title: Optional[str] = None


def create_country_response(country):
    return CountryResponse(id=country.id, title=country.title)
