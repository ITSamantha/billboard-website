import datetime
from typing import ClassVar

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: int


class BaseEntityTime(BaseEntity):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime
