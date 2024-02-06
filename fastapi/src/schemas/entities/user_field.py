from pydantic import BaseModel
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class UserField(BaseEntity):
    type: str
    title: str

    order: int
