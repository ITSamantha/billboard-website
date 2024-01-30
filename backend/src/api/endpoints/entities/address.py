from pydantic import BaseModel
from typing import ClassVar, Union


class Address(BaseModel):
    id: ClassVar[int]

    address: ClassVar[str]
    country: Union[ClassVar[str], None]
    city: Union[ClassVar[str], None]
    street: Union[ClassVar[str], None]
    house: Union[ClassVar[str], None]
    flat: Union[ClassVar[str], None]

    longitude: Union[ClassVar[float], None]
    latitude: Union[ClassVar[float], None]
