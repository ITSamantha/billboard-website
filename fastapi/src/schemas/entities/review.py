from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntityTime


class Review(BaseEntityTime):
    advertisement_id: int
    user_id: int

    text: str
    rating: int


class ReviewResponse(Review, BaseResponseSchema):
    pass


class ReviewCreate(Review):
    pass


class ReviewUpdate(Review):
    pass
