from typing import Optional, List, Dict, Union, Any

from fastapi.exceptions import RequestValidationError
from pydantic import field_validator, validator, BaseConfig, ConfigDict, root_validator, model_validator, Field

from src.api.payloads.base import BasePayload
from src.schemas import BaseResponseSchema, Category, Filter, FilterValue, Address, AddressCreate
from src.schemas.entities.base import BaseEntity


class Advertisement(BasePayload):
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


class AdvertisementPost(BasePayload):
    title: str  # for validation
    user_description: str
    categories: Optional[List[int]]  # essential?
    filters: Optional[Dict[int, Union[str, int]]]  # Filter, FilterValue
    ad_type_id: int
    address: Optional[AddressCreate]
    address_id: Optional[int]
    price: float


class AdvertisementUpdate(Advertisement):
    pass
