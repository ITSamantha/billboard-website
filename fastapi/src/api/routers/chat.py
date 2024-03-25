from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.payloads.base import BasePayload
from src.api.responses.api_response import ApiResponse
from src.api.transformers.chat.chat_transformer import ChatTransformer
from src.database.session_manager import db_manager
from sqlalchemy.orm import joinedload
from src.database.models.entities.chat_user import ChatUser
from src.database.models.entities.chat import Chat
from sqlalchemy.future import select
from src.utils.transformer import transform
from src.utils.validator import Validator
from src.repository.crud.base_crud_repository import SqlAlchemyRepository

router = APIRouter(
    prefix="/chats",
)


@router.get("")
async def index(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    async with db_manager.get_session() as session:
        q = select(Chat)\
            .filter(Chat.id.in_(select(ChatUser.chat_id).where(ChatUser.user_id == request.state.user.id).distinct()))\
            .options(joinedload(Chat.messages))  # todo limit messages
        res = await session.execute(q)

        chats = res.unique().scalars().all()
    return ApiResponse.payload(transform(
        chats,
        ChatTransformer().include(['messages'])
    ))


@router.get('/{chat_id}')
async def find(chat_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    async with db_manager.get_session() as session:
        #  todo chat must have chat_user with request.state.user.id == user_id
        q = select(Chat)\
            .where(Chat.id == chat_id)\
            .options(joinedload(Chat.messages))  # todo limit messages
        res = await session.execute(q)
        chat = res.scalar()

    if not chat:
        return ApiResponse.error('Chat is not found', 404)

    return ApiResponse.payload(transform(
        chat,
        ChatTransformer().include(['messages'])
    ))


@router.post('')
async def store(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    validator = Validator(await request.json(), {
        "user_id": ["required", "integer"],
    }, {}, BasePayload())
    payload = validator.validated()

    #  check if the chat between these users already exists
    async with db_manager.get_session() as session:
        subquery1 = select(ChatUser.chat_id).where(ChatUser.user_id == payload.user_id).distinct()
        subquery2 = select(ChatUser.chat_id).where(ChatUser.user_id == request.state.user.id).distinct()
        q = select(Chat)\
            .where(Chat.id.in_(subquery1))\
            .where(Chat.id.in_(subquery2))

        res = await session.execute(q)
        chats = res.unique().scalars().all()

    if chats:
        return ApiResponse.error('Chat between these users already exists')
    #  create chat
    chat: Chat = await SqlAlchemyRepository(db_manager.get_session, Chat).create({})
    #  add users to chat
    await SqlAlchemyRepository(db_manager.get_session, ChatUser).bulk_create([
        {
            'chat_id': chat.id,
            'user_id': payload.user_id,
        },
        {
            'chat_id': chat.id,
            'user_id': request.state.user.id,
        }
    ])

    return ApiResponse.payload(transform(
        chat,
        ChatTransformer()
    ))
