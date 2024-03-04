from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.characteristics.city import City, create_city
from src.schemas.characteristics.country import Country, create_country
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

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


class AddressShort(BaseModel):
    id: int
    address: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None


def create_short_address(address: models.Address) -> AddressShort:
    return AddressShort(id=address.id,
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


def create_address_create(address):
    result = AddressCreate()
    result.address = address.address
    result.flat = address.flat
    result.house = address.house
    result.street = address.street
    result.latitude = address.latitude
    result.longitude = address.longitude
    result.city_id = address.city_id
    result.country_id = address.country_id
    return result


def validate_address_create(address):
    validator = Validator(address, {
        'address': [Rules.REQUIRED, Rules.STRING],
        'city_id': [Rules.INTEGER],
        'country_id': [Rules.INTEGER],
        'street': [Rules.STRING],
        'house': [Rules.STRING],
        'flat': [Rules.STRING],
        'longitude': [Rules.FLOAT],
        'latitude': [Rules.FLOAT]
    }, {}, AddressCreate())

    address: AddressCreate = validator.validated()
    return address
