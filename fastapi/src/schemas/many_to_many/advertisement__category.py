from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.entities.advertisement import Advertisement
from src.schemas.entities.category import Category


class AdvertisementCategory(BaseModel):
    # advertisement_id: int
    advertisement: Advertisement
    # category_id: int
    category: Category


class AdvertisementCategoryCreate(BasePayload):
    advertisement_id: int
    category_id: int
