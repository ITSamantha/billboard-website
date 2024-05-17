from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.config.app.config import settings_app
import stripe

from src.database.models import Tariff
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
def success(request: Request, session_id: str):
    session = stripe.checkout.Session.retrieve(session_id)
    with open('huy', 'a') as f:
        f.write(session.metadata)
    return RedirectResponse("https://otiva.space?success")


@router.get('/fail')
def success():
    return RedirectResponse("https://otiva.space?fail")
