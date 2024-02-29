import datetime
from typing import Optional

from pydantic import BaseModel

from src.database import models


class Token(BaseModel):
    id: int
    access_token: str
    token_type: str

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_token(token: models.Token) -> Token:
    return Token(id=token.id,
                 access_token=token.access_token,
                 token_type=token.token_type,
                 created_at=token.created_at,
                 updated_at=token.updated_at,
                 deleted_at=token.deleted_at)
