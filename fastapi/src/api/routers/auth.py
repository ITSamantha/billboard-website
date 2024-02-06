from fastapi import APIRouter, Depends, Request

from src.api.dependencies.router import IsAuthenticated
from src.api.responses.api_response import ApiResponse
from src.api.use_cases.auth import *
from src.api.payloads.auth import *

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register(payload: RegisterPayload):
    # todo check payload here should be validated already
    user = await RegisterUseCase.register(payload)
    return ApiResponse.payload(user)  # todo serialize user?


@router.post("/login")
async def login(payload: LoginPayload):
    try:
        access_token, token_type = await LoginUseCase.login(payload)
    except Exception as e:
        return ApiResponse.error(str(e), 401)

    response = ApiResponse.payload(
        data={
            'access_token': access_token,
            'token_type': token_type,
        }
    )

    response.set_cookie(
        key="jwt",
        value=access_token,
        httponly=True,
        # max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # Cookie expiration time in seconds
        # expires=ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # Cookie expiration time in seconds
        # secure=False,  # Set to True if using HTTPS
        # same_site="none",  # Set to "Lax" or "Strict" if needed for CSRF protection
    )

    return response


@router.post("/logout", dependencies=[Depends(IsAuthenticated())])
async def logout():
    #  todo revoke token cause unsetting it is not enough??
    response = ApiResponse.success('You have successfully logged out.')
    response.set_cookie(
        key="jwt",
        value='',
        httponly=True,
    )
    return response
