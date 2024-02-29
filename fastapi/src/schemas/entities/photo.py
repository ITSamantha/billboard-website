from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class Photo(BaseModel):
    id: int
    photo_path: str
    photo_thumb: Optional[str] = None


def create_photo(photo: models.Photo) -> Photo:
    return Photo(id=photo.id,
                 photo_path=photo.photo_path,
                 photo_thimb=photo.photo_thumb)


class PhotoCreate(BasePayload):
    photo_path: str
    photo_thumb: Optional[str] = None


class PhotoUpdate(BasePayload):
    photo_path: Optional[str] = None
    photo_thumb: Optional[str] = None
