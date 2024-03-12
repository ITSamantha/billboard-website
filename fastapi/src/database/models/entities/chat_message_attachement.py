from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class ChatMessageAttachement(Base):
    __tablename__ = "chat_message_attachements"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    chat_message_id: Mapped[int] = mapped_column(ForeignKey("chat_messages.id"))
    # file_id: Mapped[int] = mapped_column(ForeignKey('files.id')) todo
т