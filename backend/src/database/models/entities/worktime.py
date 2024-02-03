import datetime
from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.entities.base import BaseEntityModel
from src.schemas.entities.base import BaseEntity


class Worktime(BaseEntityModel):
    weekday_id: ClassVar[int]
    advertisement_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('advertisement.id'), nullable=False)

    start_time: ClassVar[datetime.time]
    end_time: ClassVar[datetime.time]
