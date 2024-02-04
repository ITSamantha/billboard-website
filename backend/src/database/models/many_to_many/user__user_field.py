from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class UserUserField(Base):
    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user.id'), nullable=False)
    user_field_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey('user_field.id'), nullable=False)
