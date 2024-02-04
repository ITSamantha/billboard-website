from typing import ClassVar

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import BaseEntityModelTime


class UserNotification(BaseEntityModelTime):
    __tablename__ = "user_notification"

    title: Mapped[ClassVar[str]] = mapped_column(String(256), nullable=False)
    description: Mapped[ClassVar[str]] = mapped_column(Text, nullable=False)

    notification_type: Mapped[ClassVar[str]] = mapped_column(Text,
                                                             nullable=False)  # ПОЛИМОРФНЫЙ. "models/entities/category/booking"
    notification_content: Mapped[ClassVar[int]] = mapped_column(Text,
                                                                nullable=False)  # ПОЛИМОРФНЫЙ  # TODO: Тюм, разберись, пж

    user_id: Mapped[ClassVar[int]] = mapped_column(ForeignKey("user.id"), nullable=False)
