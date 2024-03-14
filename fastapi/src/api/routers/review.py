from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.review_transformer import ReviewTransformer
from src.utils.transformer import transform
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.entities.review import ReviewUpdate
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],

)


@router.get(path='/{review_id}', response_model=ApiResponse)
async def get_review(review_id: int, request: Request, auth: Auth = Depends()):
    """Get exact review information. """

    await auth.check_access_token(request)

    try:
        review: models.Review = await SqlAlchemyRepository(db_manager.get_session, models.Review)\
            .get_single(id=review_id)

        if not review:
            raise Exception("Review is not found.")

        return ApiResponse.payload(transform(review, ReviewTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


# TODO: GET MY REVIEWS
# TODO:GET USER REVIEWS


@router.post(path='/')
async def create_advertisement_review(request: Request, auth: Auth = Depends()):
    """Create review for advertisement. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'advertisement_id': [Rules.REQUIRED, Rules.INTEGER],
        'text': [Rules.REQUIRED, Rules.STRING],
        'rating': [Rules.REQUIRED, Rules.FLOAT],  # TODO: 0<=x<=5
    })

    payload = validator.validated()

    try:
        if await SqlAlchemyRepository(db_manager.get_session, models.Review)\
                .get_single(advertisement_id=payload["advertisement_id"]):
            raise Exception('The review for this advertisement has already been published.')

        review: models.Review = await SqlAlchemyRepository(db_manager.get_session, models.Review)\
            .create(validator.all() | {"user_id": request.state.user.id})

        return ApiResponse.payload(transform(review, ReviewTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.put(path='/{review_id}')
async def update_review(review_id: int, request: Request, auth: Auth = Depends()):
    """Update review by id. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'text': [Rules.STRING],
        'rating': [Rules.FLOAT]  # TODO: 0<=x<=5
    }, {}, ReviewUpdate())

    payload: ReviewUpdate = validator.validated()

    try:
        # todo : check existence
        review: models.Review = await SqlAlchemyRepository(db_manager.get_session, models.Review)\
            .update(payload.all(), id=review_id)

        return ApiResponse.payload(transform(review, ReviewTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))
