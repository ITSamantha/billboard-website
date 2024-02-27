from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base



class AdStatus(Base):
    ACTIVE = 1
    BLOCKED = 2
    PAID = 3
    NOT_PAID = 4
    MEOW = 5

    __tablename__ = "ad_status"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    is_shown: Mapped[bool] = mapped_column(default=False, nullable=False, index=True)

    def __repr__(self) -> str:
        return f"AdStatus(id={self.id}, title={self.title}, is_shown={self.is_shown})"
