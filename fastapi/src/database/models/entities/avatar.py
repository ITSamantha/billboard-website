from fastapi import Request

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Avatar(Base):
    __tablename__ = "avatar"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    photo_path: Mapped[str] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"Avatar(id={self.id}, photo_path={self.photo_path})"

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
