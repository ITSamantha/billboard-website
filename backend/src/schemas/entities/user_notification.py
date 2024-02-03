import datetime
from pydantic import BaseModel
from typing import ClassVar

from src.schemas.entities.base import BaseEntityTime


class UserNotification(BaseEntityTime):
    title: ClassVar[str]
    description: ClassVar[str]

    notification_type: ClassVar[str]  # 'models/entities/category/booking'
    notification_content: ClassVar[int]

    user_id: ClassVar[int]
