from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas import BaseResponseSchema, create_country_response, create_city_response, CityResponse, CountryResponse
from src.schemas.entities.base import BaseEntity


class Address(BasePayload):
    address: str
    country: Optional[int] = None
    city: Optional[int] = None
    street: Optional[str] = None
    house: Optional[str] = None
    flat: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None


class AddressResponse(BaseModel):
    id: int
    address: str
    country: Optional[CountryResponse] = None
    city: Optional[CityResponse] = None
    street: Optional[str] = None
    house: Optional[str] = None
    flat: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None


def create_address_response(address):
    return AddressResponse(id=address.id, address=address.address,
                           country=create_country_response(address.country) if address.country else None,
                           city=create_city_response(address.city) if address.city else None,
                           street=address.street, house=address.house, flat=address.flat,
                           longitude=address.longitude, latitude=address.latitude)


class AddressShort(BaseEntity, BaseResponseSchema):
    address: str
    longitude: float
    latitude: float


class AddressCreate(Address):
    pass


class AddressUpdate(Address):
    pass
