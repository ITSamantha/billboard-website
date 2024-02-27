import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas import AddressResponse, UserShortResponse, AdStatus, AdType, create_address_response, create_ad_status, \
    create_ad_type, create_user_short_response


class AdvertisementResponse(BaseModel):
    id: int
    title: str
    user_description: str
    address: AddressResponse
    user: UserShortResponse
    ad_status: AdStatus
    ad_type: AdType
    price: Optional[float]

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_advertisement_response(ad):
    return AdvertisementResponse(id=ad.id, title=ad.title, user_description=ad.user_description,
                                 address=create_address_response(ad.address), user=create_user_short_response(ad.user),
                                 ad_status=create_ad_status(ad.ad_status), ad_type=create_ad_type(ad.ad_type),
                                 price=ad.price, created_at=ad.created_at, updated_at=ad.updated_at,
                                 deleted_at=ad.deleted_at)


class Advertisement(BasePayload):
    title: str
    user_description: str
    address_id: Optional[int]

    user_id: int

    ad_status_id: int
    ad_type_id: int  # booking, sell

    price: Optional[float]


class AdvertisementCreate(Advertisement):
    pass


"""
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
"""
