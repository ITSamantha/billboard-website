from pydantic import BaseModel
from typing import ClassVar


class AdvertisementFilterValue(BaseModel):
    advertisement_id: ClassVar[int]
    filter_value_id: ClassVar[int]
