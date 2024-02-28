from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload


class Country(BaseModel):
    id: int
    title: str


class CountryUpdate(BasePayload):
    title: str


class CountryCreate(BasePayload):
    title: str


def create_country(country):
    return Country(id=country.id, title=country.title)
