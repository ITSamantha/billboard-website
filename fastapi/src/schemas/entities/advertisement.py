from typing import Optional

from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntityTime


class Advertisement(BaseEntityTime):
    title: str
    user_description: str

    address_id: Optional[int]

    user_id: int

    advertisement_status_id: int
    advertisement_type_id: int  # booking, sell

    price: Optional[float]


class AdvertisementResponse(Advertisement, BaseResponseSchema):
    pass


class AdvertisementCreate(Advertisement):
    pass


class AdvertisementUpdate(Advertisement):
    pass
