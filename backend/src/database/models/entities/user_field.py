from pydantic import BaseModel
from typing import ClassVar

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class UserField(BaseEntityModel):
    type: ClassVar[str]
    title: ClassVar[str]

    order: ClassVar[int]
