from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/test",
)


@router.post('/account')
async def me_account(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    account = await request.state.user.get_account()
    data = await request.json()
    type_id = data['type_id']
    amount = data['amount']
    await account.add_transaction(type_id, amount)

    return 'good'


@router.post('/file')
async def me_account(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    from src.utils.storage import storage
    from src.database.models.entities.file import File, Disk
    from src.api.transformers.file_transformer import FileTransformer
    data = await request.json()
    try:
        path, ext = storage.save_from_base64(data['image'], Disk.IMAGES)
    except Exception as e:
        return ApiResponse.error(str(e))
    file = await SqlAlchemyRepository(db_manager.get_session, model=File) \
        .create({
            'path': path,
            'extension': ext,
            'disk': Disk.IMAGES,
        })

    return ApiResponse.payload(transform(file, FileTransformer()))


@router.post('/valid')
async def me_account(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    from src.utils.validator import Validator
    validator = Validator(await request.json(), {
        'id': ['required', 'integer'],
        'str': ['required', 'string'],
        'images': ['required', 'list'],
        'images.id': ['required', 'integer'],
        'images.path': ['required', 'string'],
        'images.smth': ['required', 'list'],
        'images.smth.id': ['required', 'integer'],
        'images.smth.path': ['required', 'string'],
    })
    # validator.validate()

    return validator.validated()
