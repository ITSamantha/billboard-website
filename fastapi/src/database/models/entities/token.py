import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from fastapi import Request
from src.database.models.base import Base


class Token(Base):
    __tablename__ = "token"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    access_token: Mapped[str] = mapped_column(nullable=False)
    token_type: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)
