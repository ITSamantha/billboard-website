from typing import Optional, List, Dict, Union

from pydantic import BaseModel

from src.schemas import BaseResponseSchema, Category, Filter, FilterValue, Address
from src.schemas.entities.base import BaseEntity


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


class AdvertisementCreate(BaseModel):
    title: str
    user_description: str
    categories: List[int]
    filters: Dict[int, Union[str, int]]  # Filter, FilterValue
    ad_type_id: int
    address: Optional[Address]
    address_id: Optional[int]


class AdvertisementUpdate(Advertisement):
    pass
