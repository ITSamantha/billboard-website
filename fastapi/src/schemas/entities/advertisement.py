from typing import Optional

from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntityTime, BaseEntity


class Advertisement(BaseEntity):
    title: str
    user_description: str

    address_id: Optional[int]

    user_id: int

    ad_status_id: int
    ad_type_id: int  # booking, sell

    price: Optional[float]


class AdvertisementResponse(Advertisement, BaseResponseSchema):
    pass


class AdvertisementCreate(Advertisement):
    pass


class AdvertisementCreateSeller(Advertisement):
    pass


class AdvertisementUpdate(Advertisement):
    pass
