import datetime

from src.schemas.base import BaseSchema


class BaseEntity(BaseSchema):
    pass


class BaseEntityTime(BaseEntity):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

