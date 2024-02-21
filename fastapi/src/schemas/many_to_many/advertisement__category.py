from src.api.payloads.base import BasePayload
from src.schemas.base import BaseSchema


class AdvertisementCategory(BasePayload):
    advertisement_id: int
    category_id: int


class AdvertisementCategoryCreate(AdvertisementCategory):
    pass