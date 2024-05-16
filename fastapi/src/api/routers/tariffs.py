from fastapi import APIRouter, Request, Depends
from sqlalchemy import select

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.tariff_transformer import TariffTransformer
from src.database.models import Tariff
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform
from src.utils.validator import Validator

router = APIRouter(
    prefix="/tariffs",
)


@router.get("")
async def index(request: Request, auth: Auth = Depends()):
    try:
        tariffs = await SqlAlchemyRepository(db_manager.get_session, Tariff)\
            .get_multi()

        return ApiResponse.payload(transform(tariffs, TariffTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{tariff_id}")
async def find(tariff_id: int, request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)

    try:
        tariff: Tariff = await SqlAlchemyRepository(db_manager.get_session, Tariff) \
            .get_single(id=tariff_id)
        if not tariff:
            raise Exception("Tariff is not found.")

        return ApiResponse.payload(transform(tariff, TariffTransformer()))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.post("")
async def store(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'name': ['required', 'string'],
        'description': ['required', 'string'],
        'price': ['required', 'integer'],
        'available_ads': ['required', 'integer'],
    })
    data = validator.validated()
    async with db_manager.get_session() as session:
        session.add(Tariff(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available_ads=data['available_ads'],
        ))
        await session.commit()

    return ApiResponse.success('Tariff added')


@router.put("/{tariff_id}")
async def update(tariff_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'name': ['required', 'string'],
        'description': ['required', 'string'],
        'price': ['required', 'integer'],
        'available_ads': ['required', 'integer'],
    })
    data = validator.validated()
    async with db_manager.get_session() as session:
        q = select(Tariff) \
            .where(Tariff.id == tariff_id)
        res = await session.execute(q)
        tariff = res.scalar()

        tariff.name = data['name']
        tariff.description = data['description']
        tariff.price = data['price']

        await session.commit()

    return ApiResponse.success('Tariff updated')


@router.delete("/{tariff_id}")
async def destroy(tariff_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:
        await SqlAlchemyRepository(db_manager.get_session, Tariff) \
            .delete(id=tariff_id)

        return ApiResponse.success('Tariff deleted')
    except Exception as e:
        return ApiResponse.error(str(e))
