from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas import BaseResponseSchema
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
    country: Optional[int] = None
    city: Optional[int] = None
    street: Optional[str] = None
    house: Optional[str] = None
    flat: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None


def create_address_response(address):
    return AddressResponse(id=address.id, address=address.address, country=address.country, city=address.city,
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
