
from src.schemas.base import BaseSchema
from src.schemas.entities.advertisement import Advertisement
from src.schemas.entities.filter_value import FilterValue


class AdvertisementFilterValue(BaseSchema):
    # advertisement_id: int
    advertisement: Advertisement
    # filter_value_id: int
    filter_value: FilterValue


class AdvertisementFilterValueCreate(BaseSchema):
    advertisement_id: int
    filter_value_id: int
