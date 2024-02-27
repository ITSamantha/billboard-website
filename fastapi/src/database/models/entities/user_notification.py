import datetime
from typing import Optional

from fastapi import Request

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base


class UserNotification(Base):
    __tablename__ = "user_notification"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    notification_type: Mapped[str] = mapped_column(Text,
                                                   nullable=False)  # ПОЛИМОРФНЫЙ. "models/entities/category/booking"
    notification_content: Mapped[int] = mapped_column(Text,
                                                      nullable=False)  # ПОЛИМОРФНЫЙ  # TODO: Тюм, разберись, пж

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (
            f"UserNotification(id={self.id}, title={self.title}, description={self.description}, user_id={self.user_id})")
