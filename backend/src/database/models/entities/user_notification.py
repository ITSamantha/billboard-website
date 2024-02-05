from typing import ClassVar

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModelTime


class UserNotification(AbstractBaseEntityModelTime):
    __tablename__ = "user_notification"

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    notification_type: Mapped[str] = mapped_column(Text,
                                                             nullable=False)  # ПОЛИМОРФНЫЙ. "models/entities/category/booking"
    notification_content: Mapped[int] = mapped_column(Text,
                                                                nullable=False)  # ПОЛИМОРФНЫЙ  # TODO: Тюм, разберись, пж

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="notifications", uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"UserNotification(id={self.id}, title={self.title}, description={self.description}, user_id={self.user_id})")
