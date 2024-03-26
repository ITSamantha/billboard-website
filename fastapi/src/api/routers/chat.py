from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.payloads.base import BasePayload
from src.api.responses.api_response import ApiResponse
from src.api.transformers.chat.chat_message_transformer import ChatMessageTransformer
from src.api.transformers.chat.chat_transformer import ChatTransformer
from src.database.models import ChatMessage
from src.database.session_manager import db_manager
from sqlalchemy.orm import joinedload
from src.database.models.entities.chat_user import ChatUser
from src.database.models.entities.chat import Chat
from sqlalchemy.future import select
from src.utils.transformer import transform
from src.utils.validator import Validator
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.pubsub import PubSub, PubSubEvent, PubSubEvents

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


@router.post('/{chat_id}/messages')
async def store_message(chat_id, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json() | {'chat_id': chat_id}, {
        'text': ['required', 'string'],
    }, {}, BasePayload())
    payload = validator.validated()

    # chat must have current user as ChatUser
    async with db_manager.get_session() as session:
        q = select(Chat) \
            .options(joinedload(Chat.chat_users))\
            .where(Chat.id == chat_id)
        res = await session.execute(q)
        chat: Chat = res.scalar()

    current_chat_user: ChatUser = next(filter(lambda cu: cu.user_id == request.state.user.id, chat.chat_users))

    if not chat:
        return ApiResponse.error('Chat does not exists.')
    if not current_chat_user:
        return ApiResponse.error('User does not belongs to this chat.')

    message: ChatMessage = await SqlAlchemyRepository(db_manager.get_session, ChatMessage).create({
        'chat_user_id': current_chat_user.id,
        'chat_id': chat_id,
        'text': payload.text,
        'seen_at': None,
    })

    transformed_message = transform(message, ChatMessageTransformer())

    notifications = {}
    for chat_user in chat.chat_users:
        # do not notify sender
        if chat_user.user_id == request.state.user.id:
            continue
        notifications[f'notifications:{chat_user.user_id}'] = PubSubEvent(PubSubEvents.NEW_MESSAGE, transformed_message)

    await PubSub.publish(notifications)  # todo to queue

    return ApiResponse.payload(transformed_message)
