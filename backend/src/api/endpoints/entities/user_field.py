from pydantic import BaseModel
from typing import ClassVar


class UserField(BaseModel):
    id: ClassVar[int]
    type: ClassVar[str]
    title: ClassVar[str]
