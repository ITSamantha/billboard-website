from typing import List
from fastapi import Request
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base


# TODO: ADD TO ADMIN
class UserField(Base):
    __tablename__ = "user_field"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    type: Mapped[str] = mapped_column(String(128), nullable=False)

    title: Mapped[str] = mapped_column(String(128), nullable=False)

    order: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"UserField(id={self.id}, type={self.type}, title={self.title}, order={self.order})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
