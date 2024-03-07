from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

from src.database.models.base import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    chat_user_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    text: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    seen_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    chat_user: Mapped["ChatUser"] = relationship(uselist=False, lazy="selectin")
    attachements: Mapped["ChatMessageAttachement"] = relationship(uselist=True, lazy="selectin")
