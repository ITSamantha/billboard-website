import datetime
from typing import ClassVar


class AdPhoto:
    photo_id: ClassVar[int]
    advertisement_id: ClassVar[int]
    is_main: ClassVar[bool]
