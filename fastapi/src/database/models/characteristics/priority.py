from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base



class Priority(Base):
    __tablename__ = "priority"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    priority: Mapped[int] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"Priority(id={self.id}, title={self.title})"
