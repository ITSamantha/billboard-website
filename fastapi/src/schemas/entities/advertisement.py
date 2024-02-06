from typing import ClassVar, Union

from src.schemas.entities.base import BaseEntityTime


class Advertisement(BaseEntityTime):
    title: str
    user_description: str

    address_id: Union[int, None]

    user_id: int

    advertisement_status_id: int
    advertisement_type_id: int  # booking, sell

    price: Union[float, None]
