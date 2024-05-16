import datetime

from fastapi import APIRouter, Request, Depends
from sqlalchemy import select, delete

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database.models import CategoryFilter, File, Category, PhoneCode, User
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.validator import Validator

router = APIRouter(
    prefix="/phone",
)


@router.post("/send_code")
async def send(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    if request.state.user.phone_verified_at:
        return ApiResponse.error('Phone is already verified')

    async with db_manager.get_session() as session:
        session.add(PhoneCode(
            user_id=request.state.user.id,
            code='1111',
            expires_at=datetime.datetime.now() + datetime.timedelta(minutes=5)
        ))
        await session.commit()

    return ApiResponse.success('Code successfully sent')


@router.post("/verify")
async def verify(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    if request.state.user.phone_verified_at:
        return ApiResponse.error('Phone is already verified')
    validator = Validator(await request.json(), {
        'code': ['required', 'string'],
    })
    data = validator.validated()

    async with db_manager.get_session() as session:
        q = select(PhoneCode) \
            .where(PhoneCode.code == data['code']) \
            .where(PhoneCode.user_id == request.state.user.id)
        res = await session.execute(q)
        phone_code = res.scalar()

        if not phone_code:
            return ApiResponse.error('Invalid code.')
        if phone_code.expires_at < datetime.datetime.now():
            return ApiResponse.error('Code has expired.')

        q = delete(PhoneCode) \
            .filter(PhoneCode.id == phone_code.id)
        await session.execute(q)

        await session.commit()

    await SqlAlchemyRepository(db_manager.get_session, User) \
        .update(data={"phone_verified_at": datetime.datetime.now(), 'available_ads': request.state.user.available_ads + 5}, id=request.state.user.id)

    return ApiResponse.success('Phone has been successfully verified.')
