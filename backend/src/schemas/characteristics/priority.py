from typing import ClassVar

from src.schemas.characteristics.base import BaseCharacteristic


# ad priority
class Priority(BaseCharacteristic):
    priority: ClassVar[int]
