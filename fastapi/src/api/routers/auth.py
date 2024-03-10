from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.use_cases.auth import *
from src.api.payloads.auth import *
from src.database.models.characteristics.user_status import UserStatus
from src.database.models.entities.user import User
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=None)
async def register(request: Request):
    validator = Validator(await request.json(), {
        'first_name': [Rules.REQUIRED, Rules.STRING],
        'last_name': [Rules.REQUIRED, Rules.STRING],
        'email': [Rules.REQUIRED, Rules.STRING],
        'password': [Rules.REQUIRED, Rules.STRING],
        'phone_number': [Rules.REQUIRED, Rules.STRING]
    }, {}, RegisterPayload())
    payload = validator.validated()
    payload.user_status_id = UserStatus.ACTIVE
    try:
        user: User = await RegisterUseCase.register(
            payload.only(['first_name', 'last_name', 'email', 'password', 'phone_number']) | {
                "user_status_id": UserStatus.ACTIVE})
    except Exception as e:
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'user_id': user.id
    })


@router.post("/login")
async def login(request: Request):
    validator = Validator(await request.json(), {
        'email': [Rules.REQUIRED],
        'password': [Rules.REQUIRED],
    }, {}, LoginPayload())
    payload = validator.validated()
    try:
        access_token, refresh_token = await LoginUseCase.login(payload)
    except Exception as e:
        return ApiResponse.error(str(e), 401)

    return format_jwt_response(access_token, refresh_token)


@router.post("/logout")
async def logout(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    #  todo revoke token cause unsetting it is not enough??
    response = ApiResponse.success('You have successfully logged out.')
    response.delete_cookie('jwt_access_token')
    response.delete_cookie('jwt_refresh_token')
    return response


@router.post('/refresh')
async def refresh(request: Request, auth: Auth = Depends()):
    payload = await auth.check_refresh_token(request)  # todo dto for payload
    try:
        access_token, refresh_token = await RefreshUseCase.refresh(payload)
    except Exception as e:
        return ApiResponse.error(str(e), 401)

    return format_jwt_response(access_token, refresh_token)


def format_jwt_response(access_token: str, refresh_token: str):
    response = ApiResponse.payload(
        data={
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
    )

    response.set_cookie(
        key="jwt_access_token",
        value=access_token,
        httponly=True,
    )
    response.set_cookie(
        key="jwt_refresh_token",
        value=refresh_token,
        httponly=True,
    )

    return response
