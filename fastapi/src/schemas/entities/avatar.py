from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class Avatar(BaseModel):
    id: int
    photo_path: str
    photo_thumb: Optional[str] = None


def create_avatar(avatar: models.Avatar) -> Avatar:
    return Avatar(id=avatar.id,
                  photo_path=avatar.photo_path,
                  photo_thumb=avatar.photo_thumb)


class AvatarUpdate(BasePayload):
    photo_path: Optional[str] = None
    photo_thumb: Optional[str] = None


class AvatarCreate(BaseModel):
    photo_path: str
    photo_thumb: Optional[str] = None
