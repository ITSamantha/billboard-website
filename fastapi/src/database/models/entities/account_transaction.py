from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
import datetime
from src.database.models.base import Base
from src.database.models.entities.account import Account
from src.database.models.entities.account_transaction_type import AccountTransactionType


class AccountTransaction(Base):
    __tablename__ = "account_transactions"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    type_id: Mapped[int] = mapped_column((ForeignKey('account_transaction_types.id')))
    amount: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())

    account: Mapped["Account"] = relationship(uselist=False, lazy="selectin", back_populates="transactions")
    type: Mapped["AccountTransactionType"] = relationship(uselist=False, lazy="selectin")
