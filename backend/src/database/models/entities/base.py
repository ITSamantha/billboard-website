import datetime
from typing import ClassVar

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import AbstractModel


class BaseEntityModel(AbstractModel):
    __abstract__ = True


class BaseEntityModelTime(BaseEntityModel):
    __abstract__ = True

    created_at: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    updated_at: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
    deleted_at: Mapped[ClassVar[datetime.datetime]] = mapped_column(nullable=False)
