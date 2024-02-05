from typing import ClassVar, Union, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.transactions.base import AbstractBaseTransactionModel


class Transaction(AbstractBaseTransactionModel):
    __tablename__ = "transaction"

    transaction_type_id: Mapped[int] = mapped_column(
        ForeignKey("transaction_type.id"), nullable=False)  # бронирование, объявление, ...
    transaction_type: Mapped["TransactionType"] = relationship(back_populates="transactions", uselist=False,
                                                               lazy="selectin")

    remote_id: Mapped[Optional[str]] = mapped_column(nullable=False)

    advertisement_id: Mapped[Optional[int]] = mapped_column(nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="transactions", uselist=False, lazy="selectin")
