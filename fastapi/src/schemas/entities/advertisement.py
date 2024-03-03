import datetime
from typing import Optional, List

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas.characteristics.ad_status import AdStatus, create_ad_status
from src.schemas.characteristics.ad_type import AdType, create_ad_type
from src.schemas.entities import Address, create_address, AddressCreate
from src.schemas.entities.ad_tag import AdTag, create_ad_tag
from src.schemas.entities.user import UserShort, create_user_short


class Advertisement(BaseModel):
    id: int
    title: str
    user_description: str
    address: Address
    user: UserShort
    ad_status: AdStatus
    ad_type: AdType
    price: Optional[float]

    ad_tags: Optional[List[AdTag]]

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_advertisement(ad):
    # TODO:  CREATE RELATION ATTRS HERE AS IN MODEL
    return Advertisement(id=ad.id,
                         title=ad.title,
                         user_description=ad.user_description,
                         address=create_address(ad.address) if ad.address else None,
                         user=create_user_short(ad.user) if ad.user else None,
                         ad_status=create_ad_status(ad.ad_status) if ad.ad_status else None,
                         ad_type=create_ad_type(ad.ad_type) if ad.ad_type else None,
                         ad_tags=[create_ad_tag(tag) for tag in ad.ad_tags],
                         price=ad.price,
                         created_at=ad.created_at,
                         updated_at=ad.updated_at,
                         deleted_at=ad.deleted_at)


class AdvertisementShort(BaseModel):
    id: int
    title: str
    user_description: str
    user: UserShort


class AdvertisementCreate(BasePayload):
    title: str
    user_description: str
    user_id: int
    ad_type_id: int
    ad_status_id: int
    price: float
    address_id: int
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_advertisement_create(ad):
    advertisement = AdvertisementCreate()

    advertisement.title = ad.title
    advertisement.user_description = ad.user_description
    advertisement.ad_type_id = ad.ad_type_id
    advertisement.price = ad.price
    advertisement.address_id = ad.address_id

    return advertisement


class AdvertisementPost(BasePayload):
    title: str
    user_description: str

    categories: List[int]
    ad_tags: Optional[List[str]] = None

    ad_type_id: int

    # ad_status_id: int

    price: float

    address: Optional[AddressCreate] = None
    address_id: Optional[int] = None

    ad_photos: Optional[List["AdPhoto"]] = None

    # worktimes?
