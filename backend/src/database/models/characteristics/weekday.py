from typing import ClassVar, Optional, List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class Weekday(AbstractCharacteristicModel):
    __tablename__ = "weekday"

    short_title: Mapped[Optional[ClassVar[str]]] = mapped_column(String(8), unique=True)
    order: Mapped[ClassVar[int]] = mapped_column()

    worktimes: Mapped[List["Worktime"]] = relationship(back_populates="weekday", uselist=True)

    def __repr__(self) -> str:
        return f"Weekday(id={self.id}, title={self.title}, short_title={self.short_title}, order={self.order})"
