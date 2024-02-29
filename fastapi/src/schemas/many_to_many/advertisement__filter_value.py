from src.schemas import Advertisement, FilterValue
from src.schemas.base import BaseSchema


class AdvertisementFilterValue(BaseSchema):
    # advertisement_id: int
    advertisement: Advertisement
    # filter_value_id: int
    filter_value: FilterValue


class AdvertisementFilterValueCreate(BaseSchema):
    advertisement_id: int
    filter_value_id: int
