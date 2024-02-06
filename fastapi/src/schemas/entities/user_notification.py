import datetime
from pydantic import BaseModel
from typing import ClassVar

from src.schemas.entities.base import BaseEntityTime


class UserNotification(BaseEntityTime):
    title: str
    description: str

    notification_type: str  # "models/entities/category/booking"
    notification_content: int

    user_id: int
