from pydantic import BaseModel
from typing import ClassVar

from src.schemas.entities.base import BaseEntity


class UserField(BaseEntity):
    type: ClassVar[str]
    title: ClassVar[str]

    order: ClassVar[int]
