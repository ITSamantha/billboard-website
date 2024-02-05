from typing import ClassVar, Union

from src.schemas.transactions.base import BaseTransaction


class Transaction(BaseTransaction):
    transaction_type_id: int  # бронирование, объявление, ...

    remote_id: Union[ClassVar[str], None]

    advertisement_id: Union[ClassVar[int], None]
