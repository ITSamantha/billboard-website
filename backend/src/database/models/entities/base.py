import datetime
from typing import ClassVar

from src.database.models.base import AbstractModel


class BaseEntityModel(AbstractModel):
    pass


class BaseEntityModelTime(BaseEntityModel):
    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
