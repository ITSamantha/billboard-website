from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class TransactionType(BaseModel):
    id: int
    title: str


def create_transaction_type(type: models.TransactionType) -> TransactionType:
    return TransactionType(id=type.id, title=type.title)


class TransactionTypeCreate(BasePayload):
    title: str


class TransactionTypeUpdate(BasePayload):
    title: str
