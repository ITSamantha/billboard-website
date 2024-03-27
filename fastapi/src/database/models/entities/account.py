from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
import datetime
from src.database.models.base import Base
from typing import List
from src.database.models.entities.user import User
from src.database.models.entities.account_transaction import AccountTransaction


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())

    transactions: Mapped[List["AccountTransaction"]] = relationship(uselist=True, lazy="selectin", back_populates="account")
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin", back_populates="account")
