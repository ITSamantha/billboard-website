from typing import Optional

from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class Address(BaseEntity):
    address: str
    country: Optional[int]
    city: Optional[int]
    street: Optional[str]
    house: Optional[str]
    flat: Optional[str]

    longitude: Optional[float]
    latitude: Optional[float]


class AddressResponse(Address, BaseResponseSchema):
    pass


class AddressCreate(Address):
    pass


class AddressUpdate(Address):
    pass
