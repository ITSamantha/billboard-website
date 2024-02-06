from pydantic import BaseModel
from typing import ClassVar


class AdvertisementFilterValue(BaseModel):
    advertisement_id: int
    filter_value_id: int
