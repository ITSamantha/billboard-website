from typing import Optional
from fastapi import Request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    transaction_type_id: Mapped[int] = mapped_column(
        ForeignKey("transaction_type.id"), nullable=False)  # бронирование, объявление, ...
    transaction_type: Mapped["TransactionType"] = relationship(uselist=False,
                                                               lazy="selectin")

    remote_id: Mapped[Optional[str]] = mapped_column(nullable=False)

    advertisement_id: Mapped[Optional[int]] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(uselist=False, lazy="selectin")
