from pydantic import BaseModel

from src.schemas.base import BaseResponseSchema


class TransactionType(BaseModel):
    pass


class TransactionTypeResponse(TransactionType, BaseResponseSchema):
    pass


class TransactionTypeCreate(TransactionType):
    pass


class TransactionTypeUpdate(TransactionType):
    pass
