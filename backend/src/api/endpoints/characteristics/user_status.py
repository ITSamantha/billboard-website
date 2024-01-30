from pydantic import BaseModel
from typing import ClassVar


class UserStatus(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    is_available: ClassVar[bool]
