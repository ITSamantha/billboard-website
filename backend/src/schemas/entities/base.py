import datetime
from typing import ClassVar

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: ClassVar[int]


class BaseEntityTime(BaseEntity):
    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
