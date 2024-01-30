from pydantic import BaseModel
from typing import ClassVar


class AdvertisementCategory(BaseModel):
    advertisement_id: ClassVar[int]
    category_id: ClassVar[int]
