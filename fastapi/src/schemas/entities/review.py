import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models

from pydantic import BaseModel

from src.schemas.entities.user import UserShort, create_user_short


class Review(BaseModel):
    id: int
    text: str
    rating: float
    user: UserShort
    advertisement_id: int

    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_review(review: models.Review) -> Review:
    return Review(
        id=review.id,
        text=review.text,
        rating=review.rating,
        user=create_user_short(review.user) if review.user else None,
        advertisement_id=review.advertisement_id,
        created_at=review.created_at,
        updated_at=review.updated_at,
        deleted_at=review.deleted_at
    )


class ReviewCreate(BasePayload):
    advertisement_id: int
    user_id: int
    text: str
    rating: float
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


class ReviewUpdate(BasePayload):
    text: Optional[str]
    rating: Optional[float]
    updated_at: Optional[datetime.datetime] = None
