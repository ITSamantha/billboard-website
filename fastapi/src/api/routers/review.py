from fastapi import APIRouter

from src.api.responses.api_response import ApiResponse
from src.database.models import Review
from src.repository.crud import review_repository

router = APIRouter(
    prefix="/review",
    tags=["review"],

)


@router.get(path='/{review_id}')
async def get_review(review_id: int):
    try:
        review: Review = await review_repository.get_single(id=review_id)
    except Exception as e:
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'review': review,
    })
