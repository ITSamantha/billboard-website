import datetime
from typing import ClassVar

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import AbstractModel


class AbstractBaseEntityModel(AbstractModel):
    __abstract__ = True


class AbstractBaseEntityModelTime(AbstractBaseEntityModel):
    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    deleted_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
