import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas import UserShort, AdStatus, AdType, create_ad_status, create_ad_type, \
    create_user_short, Address, create_address


class Advertisement(BaseModel):
    id: int
    title: str
    user_description: str
    address: Address
    user: UserShort
    ad_status: AdStatus
    ad_type: AdType
    price: Optional[float]

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
                         price=ad.price,
                         created_at=ad.created_at,
                         updated_at=ad.updated_at,
                         deleted_at=ad.deleted_at)


"""
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




class AdvertisementUpdate(Advertisement):
    pass
"""
