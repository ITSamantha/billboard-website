from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    chat_message_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    # file_id: Mapped[int] = mapped_column(ForeignKey('files.id')) todo
