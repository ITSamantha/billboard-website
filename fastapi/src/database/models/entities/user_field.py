from typing import ClassVar, List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class UserField(AbstractBaseEntityModel):
    __tablename__ = "user_field"

    type: Mapped[str] = mapped_column(String(128), nullable=False)

    title: Mapped[str] = mapped_column(String(128), nullable=False)

    order: Mapped[int] = mapped_column(nullable=False)

    users: Mapped[List["User"]] = relationship(back_populates="user_fields",
                                               uselist=True, lazy="selectin", secondary="user__user_field")

    def __repr__(self) -> str:
        return (
            f"UserField(id={self.id}, type={self.type}, title={self.title}, order={self.order})")
