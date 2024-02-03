from typing import ClassVar

from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.characteristics.base import AbstractCharacteristicModel


class AdStatus(AbstractCharacteristicModel):
    __tablename__ = "ad_status"

    is_shown: Mapped[ClassVar[bool]] = mapped_column(default=False, nullable=False, index=True)
