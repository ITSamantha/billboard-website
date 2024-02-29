import datetime
from typing import Optional

from pydantic import BaseModel

from src.api.payloads.base import BasePayload
from src.database import models

from pydantic import BaseModel


class ReviewResponse(BaseModel):
    id: int
    text: str
    rating: float
    user: UserShort
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None


def create_review_response(review: models.Review):
    response = ReviewResponse(
        id=review.id,
        text=review.text,
        rating=review.rating,
        user=create_user_short(review.user),
        created_at=review.created_at
    )

    return response


class ReviewCreate(BasePayload):
    advertisement_id: int
    user_id: int
    text: str
    rating: float
    created_at: datetime.datetime


class ReviewUpdate(BasePayload):
    text: Optional[str]
    rating: Optional[float]
