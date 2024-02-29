from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


# TODO: MANY TO MANY?
class UserField(BaseModel):
    id: int
    type: str
    title: str

    order: int


def create_user_field(field: models.UserField) -> UserField:
    return UserField(id=field.id,
                     type=field.type,
                     title=field.title,
                     order=field.order)


class UserFieldCreate(BasePayload):
    type: str
    title: str

    order: int


class UserFieldUpdate(BasePayload):
    type: Optional[str] = None
    title: Optional[str] = None

    order: Optional[int] = None
