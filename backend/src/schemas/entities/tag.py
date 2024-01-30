from pydantic import BaseModel
from typing import ClassVar


class AdvertisementTag(BaseModel):
    id: ClassVar[int]
    title: ClassVar[int]
