import json

from fastapi import APIRouter
from pydantic.json_schema import model_json_schema

from src.api.responses.api_response import ApiResponse
from src.database.models import Review
from src.repository.crud import review_repository
from src.schemas import ReviewResponse, UserShort

router = APIRouter(
    prefix="/review",
    tags=["review"],

)


@router.get(path='/{review_id}')
async def get_review(review_id: int):
    try:
        review: Review = await review_repository.get_single(id=review_id)
        if review is None:
            raise Exception("No review with this id")
    except Exception as e:
        return ApiResponse.error(str(e))
    user = UserShort(
        id=review.user.id,
        first_name=review.user.first_name,
        last_name=review.user.last_name,
        avatar=review.user.avatar,
    )

    result: dict = ReviewResponse(
        id=review.id,
        text=review.text,
        rating=review.rating,
        user=user,
        created_at=review.created_at
    ).jsonify()
    return ApiResponse.payload(result)
