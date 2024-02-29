import datetime
from typing import Optional

from pydantic import BaseModel


class UserNotification(BaseModel):
    id: int
    title: str
    description: str

    notification_type: str  # "models/entities/category/booking"
    notification_content: int

    user_id: int

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None
