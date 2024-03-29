from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from src.database.models.base import Base
from typing import List
from src.database.models.entities.chat_message import ChatMessage
from src.database.models.entities.chat_user import ChatUser

from src.database.models.entities.chat_message import ChatMessage


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())

<<<<<<< HEAD
    messages: Mapped[List["ChatMessage"]] = relationship(uselist=True, lazy="selectin", back_populates="chat")
    chat_users: Mapped[List["ChatUser"]] = relationship(uselist=True, lazy='selectin', back_populates='chat')
=======
    messages: Mapped[List[ChatMessage]] = relationship(uselist=True, lazy="selectin", back_populates="chat")
>>>>>>> feature_endpoints
