from typing import ClassVar, Union

from src.database.models.entities.base import BaseEntityModelTime
from src.schemas.entities.base import BaseEntityTime


class Advertisement(BaseEntityModelTime):
    title: ClassVar[str]
    user_description: ClassVar[str]

    address_id: Union[ClassVar[int], None]

    user_id: ClassVar[int]

    advertisement_status_id: ClassVar[int]
    advertisement_type_id: ClassVar[int]  # booking, sell

    price: Union[ClassVar[float], None]
