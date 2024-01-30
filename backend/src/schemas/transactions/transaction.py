from __future__ import annotations


class Transaction:
    transaction_type_id: int  # бронирование, объявление, ...
    id: str  # uid
    remote_id: str | None
    advertisement_id: int | None
