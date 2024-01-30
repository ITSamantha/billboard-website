from pydantic import BaseModel
from typing import ClassVar


# ad priority
class Priority(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    priority: ClassVar[int]
