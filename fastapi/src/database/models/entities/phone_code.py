from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database.models.base import Base


class PhoneCode(Base):
    __tablename__ = "phone_codes"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    expires_at: Mapped[Optional[datetime]] = mapped_column(nullable=True)
