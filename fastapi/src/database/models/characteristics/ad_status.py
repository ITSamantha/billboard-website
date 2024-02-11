from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class AdStatus(AbstractCharacteristicModel):
    # ACTIVE = 1
    # BLOCKED = 2

    __tablename__ = "ad_status"

    is_shown: Mapped[bool] = mapped_column(default=False, nullable=False, index=True)

    def __repr__(self) -> str:
        return f"AdStatus(id={self.id}, title={self.title}, is_shown={self.is_shown})"
