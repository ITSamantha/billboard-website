from pydantic import BaseModel
from typing import ClassVar


class AdvertisementCategory(BaseModel):
    advertisement_id: int
    category_id: int
