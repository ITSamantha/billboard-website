from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class ChatUser(Base):
    __tablename__ = "chat_users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    chat: Mapped["Chat"] = relationship(uselist=False, lazy="selectin")
    user: Mapped[Optional["User"]] = relationship(uselist=False, lazy="selectin")

