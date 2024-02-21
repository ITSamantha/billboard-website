from typing import Optional

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


class AddressShort(BaseEntity, BaseResponseSchema):
    address: str
    longitude: float
    latitude: float


class AddressResponse(Address, BaseResponseSchema):
    pass


class AddressCreate(Address):
    pass


class AddressUpdate(Address):
    pass
