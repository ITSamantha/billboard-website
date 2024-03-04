from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models

from src.schemas.entities.photo import Photo, create_photo


# TODO: FILTER BY DELETED_AT
class AdPhoto(BaseModel):
    id: int
    # photo_id: int
    photo: Photo
    # advertisement_id: int

    is_main: bool


def create_ad_photo(photo: models.AdPhoto) -> AdPhoto:
    return AdPhoto(id=photo.id,
                   photo=create_photo(photo.photo) if photo.photo else None,
                   # advertisement_id=photo.advertisement_id,
                   is_main=photo.is_main)


class AdPhotoCreate(BasePayload):
    photo_id: int
    advertisement_id: int
    is_main: bool
