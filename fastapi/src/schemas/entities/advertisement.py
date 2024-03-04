import datetime
from typing import Optional, List

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.schemas.characteristics.ad_status import AdStatus, create_ad_status
from src.schemas.characteristics.ad_type import AdType, create_ad_type
from src.schemas.entities import Address, create_address, AddressCreate
from src.schemas.entities.ad_photo import create_ad_photo, AdPhoto
from src.schemas.entities.ad_tag import AdTag, create_ad_tag
from src.schemas.entities.category import create_category_short, CategoryShort
from src.schemas.entities.review import create_review, Review
from src.schemas.entities.user import UserShort, create_user_short
from src.utils.time import time_ago_in_words
from src.utils.validator import Validator
from src.utils.validator.validator import Rules


class Advertisement(BaseModel):
    id: int
    title: str
    user_description: str
    address: Address
    user: UserShort
    ad_status: AdStatus
    ad_type: AdType
    price: Optional[float]

    categories: Optional[List[CategoryShort]]
    ad_tags: Optional[List[AdTag]] = None
    ad_photos: Optional[List[AdPhoto]] = None
    reviews: Optional[List[Review]] = None

    bookable: bool

    created_at: Optional[datetime.datetime] = None
    created_at_str: Optional[str] = None

    updated_at: Optional[datetime.datetime] = None
    updated_at_str: Optional[str] = None

    deleted_at: Optional[datetime.datetime] = None


def create_advertisement(ad):
    # TODO:  CREATE RELATION ATTRS HERE AS IN MODEL
    if ad.deleted_at:
        return None
    return Advertisement(id=ad.id,
                         title=ad.title,
                         user_description=ad.user_description,
                         address=create_address(ad.address) if ad.address else None,
                         user=create_user_short(ad.user) if ad.user else None,
                         ad_status=create_ad_status(ad.ad_status) if ad.ad_status else None,
                         ad_type=create_ad_type(ad.ad_type) if ad.ad_type else None,
                         ad_tags=[create_ad_tag(tag) for tag in ad.ad_tags] if ad.ad_tags else None,
                         ad_photos=[create_ad_photo(photo) for photo in ad.ad_photos] if ad.ad_photos else None,
                         categories=[create_category_short(category) for category in
                                     ad.categories] if ad.categories else None,
                         reviews=[create_review(review) for review in ad.reviews if
                                  not review.deleted_at] if ad.reviews else None,
                         price=ad.price,
                         bookable=any([category.bookable for category in ad.categories]) if ad.categories else False,
                         created_at=ad.created_at,
                         created_at_str=time_ago_in_words(ad.created_at) if ad.created_at else None,
                         updated_at=ad.updated_at,
                         updated_at_str=time_ago_in_words(ad.updated_at) if ad.updated_at else None,
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
    ad_photos: Optional[List["AdPhoto"]] = None

    ad_type_id: int

    # ad_status_id: int

    price: float

    address: Optional[AddressCreate] = None
    address_id: Optional[int] = None

    # worktimes?


def validate_advertisement_post(data):
    validator = Validator(data, {
        "title": [Rules.REQUIRED, Rules.STRING],
        "user_description": [Rules.REQUIRED, Rules.STRING],
        "address_id": [Rules.NULLABLE, Rules.INTEGER, f"{Rules.FIELDS_OR}address_id,address"],
        "address": [Rules.NULLABLE, f"{Rules.FIELDS_OR}address_id,address"],
        "ad_type_id": [Rules.REQUIRED, Rules.INTEGER],
        "price": [Rules.REQUIRED, Rules.FLOAT],
        "categories": [Rules.REQUIRED, Rules.LIST],
        "ad_tags": [Rules.REQUIRED, Rules.LIST],
        "ad_photos": [Rules.REQUIRED, Rules.LIST]
        # "filters": [Rules.NULLABLE]
    }, {}, AdvertisementPost())

    payload: AdvertisementPost = validator.validated()
    return payload
