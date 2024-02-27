from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import Base


class UserStatus(Base):
    ACTIVE = 1
    BLOCKED = 2

    __tablename__ = "user_status"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    is_available: Mapped[bool] = mapped_column(default=True, nullable=False)

    def __repr__(self) -> str:
        return f"UserStatus(id={self.id}, title={self.title}, is_available={self.is_available})"
