from pydantic import BaseModel
from typing import ClassVar


class AdvertisementAdTag(BaseModel):
    advertisement_id: ClassVar[int]
    ad_tag_id: ClassVar[int]
