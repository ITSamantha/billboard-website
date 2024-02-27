from typing import List
from fastapi import Request
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Photo(Base):
    __tablename__ = "photo"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    photo_path: Mapped[str] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:
        return f"Photo(id={self.id}, photo_path={self.photo_path})"
