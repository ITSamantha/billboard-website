from typing import ClassVar, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class AdStatus(AbstractCharacteristicModel):
    ACTIVE = 1
    BLOCKED = 2

    __tablename__ = "ad_status"

    is_shown: Mapped[bool] = mapped_column(default=False, nullable=False, index=True)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="ad_status", uselist=True,
                                                                 lazy="selectin")

    def __repr__(self) -> str:
        return f"AdStatus(id={self.id}, title={self.title}, is_shown={self.is_shown})"


AdStatus.ACTIVE
AdStatus.__class__
