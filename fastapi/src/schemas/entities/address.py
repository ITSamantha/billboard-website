from typing import ClassVar, Union, Optional

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
