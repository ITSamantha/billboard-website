import datetime
from pydantic import BaseModel
from typing import ClassVar


class UserNotification(BaseModel):
    id: ClassVar[int]
    title: ClassVar[str]
    description: ClassVar[str]

    notification_type: ClassVar[str]  # 'models/entities/category/booking'
    notification_content: ClassVar[int]

    user_id: ClassVar[int]

    created_at: ClassVar[datetime.datetime]
    updated_at: ClassVar[datetime.datetime]
    deleted_at: ClassVar[datetime.datetime]
