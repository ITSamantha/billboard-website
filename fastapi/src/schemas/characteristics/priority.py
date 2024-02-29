from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models


class Priority(BaseModel):
    id: int
    title: str
    priority: int


def create_priority(priority: models.Priority) -> Priority:
    return Priority(id=priority.id, title=priority.title, priority=priority.priority)


class PriorityCreate(BasePayload):
    title: str
    priority: int


class PriorityUpdate(BasePayload):
    title: Optional[str] = None
    priority: Optional[int] = None
