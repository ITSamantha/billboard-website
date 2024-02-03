from typing import ClassVar

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.characteristics.base import AbstractCharacteristicModel


class UserStatus(AbstractCharacteristicModel):
    __tablename__ = "user_status"

    is_available: Mapped[ClassVar[bool]] = mapped_column(default=True, nullable=False)
