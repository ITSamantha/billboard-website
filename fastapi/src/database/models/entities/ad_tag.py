from typing import List
from fastapi import Request
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


# TODO: ADD TO ADMIN
class AdTag(Base):
    __tablename__ = "ad_tag"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"AdTag(id={self.id}, title={self.title})"

