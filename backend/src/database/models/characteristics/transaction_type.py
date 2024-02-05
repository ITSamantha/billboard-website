from typing import List

from sqlalchemy.orm import relationship, Mapped

from src.database.models.characteristics.base import AbstractCharacteristicModel


class TransactionType(AbstractCharacteristicModel):
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="transaction_type", uselist=True)

    def __repr__(self) -> str:
        return f"TransactionType(id={self.id}, title={self.title})"
