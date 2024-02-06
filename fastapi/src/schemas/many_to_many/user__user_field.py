from pydantic import BaseModel
from typing import ClassVar


class UserUserField(BaseModel):
    user_id: int
    user_field_id: int
