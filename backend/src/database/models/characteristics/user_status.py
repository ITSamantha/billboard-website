from typing import ClassVar, List

from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class UserStatus(AbstractCharacteristicModel):
    __tablename__ = "user_status"

    is_available: Mapped[bool] = mapped_column(default=True, nullable=False)

    users: Mapped[List["User"]] = relationship(back_populates="user_status", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"UserStatus(id={self.id}, title={self.title}, is_available={self.is_available})"
