from typing import ClassVar

from src.schemas.characteristics.base import BaseCharacteristic


# + not paid
class AdStatus(BaseCharacteristic):
    is_shown: ClassVar[bool]
