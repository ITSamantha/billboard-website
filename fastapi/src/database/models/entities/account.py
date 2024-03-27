from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
import datetime

from src.database.models.entities.account_transaction_type import AccountTransactionType
from src.database.models.base import Base
from typing import List
from src.database.models.entities.user import User
from src.database.models.entities.account_transaction import AccountTransaction
from src.database.session_manager import db_manager
from sqlalchemy import update, select


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    balance: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())

    transactions: Mapped[List["AccountTransaction"]] = relationship(uselist=True, lazy="selectin", back_populates="account")
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin", back_populates="account")

    async def add_transaction(self, type_id: int, amount: int):
        async with db_manager.get_session() as session:
            q = select(AccountTransactionType).where(AccountTransactionType.id == type_id)
            res = await session.execute(q)
            transaction_type: AccountTransactionType = res.scalar()

            if not transaction_type:
                raise Exception('Transaction type does not exists.')

            if not transaction_type.sign and amount > self.balance:
                raise Exception('Insufficient balance.')

            session.begin()

            transaction = AccountTransaction(type_id=type_id, amount=amount)
            session.add(transaction)

            new_balance = self.balance + (amount if transaction_type.sign else amount * -1)

            q = update(Account).filter(Account.id == self.id).values({Account.balance: new_balance})
            session.execute(q)

            session.commit()
