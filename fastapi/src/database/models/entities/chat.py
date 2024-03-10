from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from src.database.models.base import Base


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())

    messages: Mapped[list["ChatMessage"]] = relationship(uselist=True, lazy="selectin")
