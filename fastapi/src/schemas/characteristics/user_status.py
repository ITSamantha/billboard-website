from typing import ClassVar

from src.schemas.characteristics.base import BaseCharacteristic


class UserStatus(BaseCharacteristic):
    is_available: ClassVar[bool]
