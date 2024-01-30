from pydantic import BaseModel
from typing import ClassVar


class UserRole(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
