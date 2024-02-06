from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class AdType(AbstractCharacteristicModel):
    __tablename__ = "ad_type"

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="ad_type", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"AdType(id={self.id}, title={self.title})"
