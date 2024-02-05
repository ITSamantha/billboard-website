from typing import ClassVar, Union

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.transactions.base import AbstractBaseTransactionModel


class Transaction(AbstractBaseTransactionModel):
    transaction_type_id: Mapped[ClassVar[int]] = mapped_column(
        ForeignKey("transaction_type.id"), nullable=False)  # бронирование, объявление, ...
    transaction_type: Mapped["TransactionType"] = relationship(back_populates="transactions", uselist=False)

    remote_id: Union[ClassVar[str], None]

    advertisement_id: Union[ClassVar[int], None]
    advertisement: Mapped["Advertisement"] = relationship(back_populates="transactions", uselist=False)
