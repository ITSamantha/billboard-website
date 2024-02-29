from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas import City, Country, create_country, create_city

"""
class Address(BasePayload):
    address: str
    country: Optional[int] = None
    city: Optional[int] = None
    street: Optional[str] = None
    house: Optional[str] = None
    flat: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None
"""


class Address(BaseModel):
    id: int
    address: str
    country: Optional[Country] = None
    city: Optional[City] = None
    street: Optional[str] = None
    house: Optional[str] = None
    flat: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None


def create_address(address: models.Address) -> Address:
    return Address(id=address.id,
                   address=address.address,
                   country=create_country(address.country) if address.country else None,
                   city=create_city(address.city) if address.city else None,
                   street=address.street,
                   house=address.house,
                   flat=address.flat,
                   longitude=address.longitude,
                   latitude=address.latitude)


class ShortAddress(BaseModel):
    id: int
    address: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None


def create_short_address(address: models.Address) -> ShortAddress:
    return ShortAddress(id=address.id,
                        address=address.address,
                        longitude=address.longitude,
                        latitude=address.latitude)


class AddressCreate(BasePayload):
    address: str
    country_id: Optional[int] = None
    city_id: Optional[int] = None
    street: Optional[str] = None
    house: Optional[str] = None
    flat: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None
