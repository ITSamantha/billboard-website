from typing import ClassVar

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: ClassVar[int]
