from pydantic import BaseModel
from typing import ClassVar


class BaseCharacteristic(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]

    def __str__(self):
        return self.title
