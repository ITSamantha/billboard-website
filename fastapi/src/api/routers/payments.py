from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy import select

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.config.app.config import settings_app
import stripe

from src.database.models import Tariff, User
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.validator import Validator

stripe.api_key = settings_app.STRIPE_SECRET

router = APIRouter(
    prefix="/payments",
)


@router.post("/create")
async def create(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'tariff_id': ['required', 'integer'],
    })

    payload = validator.validated()
    tariff: Tariff = await SqlAlchemyRepository(db_manager.get_session, Tariff) \
        .get_single(id=payload['tariff_id'])
    if not tariff:
        raise Exception("Tariff is not found.")

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'USD',
                        'product_data': {
                            'name': tariff.name,
                        },
                        'unit_amount': tariff.price,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings_app.APP_URL + '/payments/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings_app.APP_URL + '/payments/fail',
            metadata={
                'tariff_id': tariff.id,
                'user_id': request.state.user.id
            }
        )

        return ApiResponse.payload({
            'url': checkout_session.url
        })
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get('/success')
async def success(request: Request, session_id: str):
    try:
        stripe_session = stripe.checkout.Session.retrieve(session_id)
    except Exception as e:
        return ApiResponse.error(str(e))

    tariff: Tariff = await SqlAlchemyRepository(db_manager.get_session, Tariff) \
        .get_single(id=int(stripe_session.metadata.tariff_id))

    async with db_manager.get_session() as session:
        q = select(User).where(User.id == int(stripe_session.metadata.user_id))
        res = await session.execute(q)
        user = res.scalar()
        user.available_ads = user.available_ads + tariff.available_ads
        await session.commit()

    return RedirectResponse("https://otiva.space/payment/success")


@router.get('/fail')
async def success():
    return RedirectResponse("https://otiva.space/payment/fail")
