from typing import ClassVar

from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.characteristics.base import AbstractCharacteristicModel


class Priority(AbstractCharacteristicModel):
    __tablename__ = "priority"

    priority: Mapped[ClassVar[int]] = mapped_column()
