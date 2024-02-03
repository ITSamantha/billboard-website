from typing import ClassVar, Optional

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.characteristics.base import AbstractCharacteristicModel


class Weekday(AbstractCharacteristicModel):
    __tablename__ = "weekday"

    short_title: Mapped[Optional[ClassVar[str]]] = mapped_column(String(8), unique=True)
    order: Mapped[ClassVar[int]] = mapped_column()
