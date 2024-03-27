from sqlalchemy.orm import Mapped, mapped_column
from src.database.models.base import Base


class AccountTransactionType(Base):
    REFILL = 1
    WITHDRAWAL = 2

    __tablename__ = "account_transaction_types"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    sign: Mapped[bool] = mapped_column(nullable=False)  # 1 for + 0 for -
