from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.models.base import Base



class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    def __repr__(self) -> str:
        return f"City(id={self.id}, title={self.title})"
