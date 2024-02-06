from pydantic import BaseModel
from typing import ClassVar


class UserUserField(BaseModel):
    user_id: ClassVar[int]
    user_field_id: ClassVar[int]
