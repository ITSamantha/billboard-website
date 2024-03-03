from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models
from src.schemas.entities.advertisement import Advertisement, create_advertisement
from src.schemas.entities.user import User, create_user


class AdFavourite(BaseModel):
    id: int
    # advertisement_id: int
    # user_id: int
    advertisement: Advertisement
    user: User


def create_ad_favourite(fav: models.AdFavourite) -> AdFavourite:
    return AdFavourite(id=fav.id,
                       advertisement=create_advertisement(fav.advertisement) if fav.advertisement else None,
                       user=create_user(fav.user) if fav.user else None)


class AdFavouriteCreate(BasePayload):
    advertisement_id: int
    user_id: int
