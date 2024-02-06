from typing import ClassVar, Union, Optional

from src.schemas.transactions.base import BaseTransaction


class Transaction(BaseTransaction):
    transaction_type_id: int  # бронирование, объявление, ...

    remote_id: Optional[str]

    advertisement_id: Optional[int]
