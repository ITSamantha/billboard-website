from typing import ClassVar, Union, Optional

from src.schemas.entities.base import BaseEntity


class Address(BaseEntity):
    address: ClassVar[str]
    country: Optional[ClassVar[int]]
    city: Optional[ClassVar[int]]
    street: Optional[ClassVar[str]]
    house: Optional[ClassVar[str]]
    flat: Optional[ClassVar[str]]

    longitude: Optional[ClassVar[float]]
    latitude: Optional[ClassVar[float]]
