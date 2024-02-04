from typing import ClassVar, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class AdStatus(AbstractCharacteristicModel):
    __tablename__ = "ad_status"

    is_shown: Mapped[ClassVar[bool]] = mapped_column(default=False, nullable=False, index=True)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="ad_status", uselist=True)

    def __repr__(self) -> str:
        return f"AdStatus(id={self.id}, title={self.title}, is_shown={self.is_shown})"
