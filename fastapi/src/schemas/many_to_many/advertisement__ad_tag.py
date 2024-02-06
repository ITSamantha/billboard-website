from pydantic import BaseModel
from typing import ClassVar


class AdvertisementAdTag(BaseModel):
    advertisement_id: int
    ad_tag_id: int
