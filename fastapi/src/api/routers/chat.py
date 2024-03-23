from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.chat.chat_transformer import ChatTransformer
from src.database.session_manager import db_manager
from sqlalchemy.orm import joinedload
from src.database.models.entities.chat_user import ChatUser
from src.database.models.entities.chat import Chat
from sqlalchemy.future import select
from src.utils.transformer import transform

router = APIRouter(
    prefix="/chats",
)


@router.get("")
async def index(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    async with db_manager.get_session() as session:
        q = select(Chat)\
            .filter(Chat.id.in_(select(ChatUser.chat_id).where(ChatUser.user_id == request.state.user.id).distinct()))\
            .options(joinedload(Chat.messages))
        res = await session.execute(q)

        chats = res.unique().scalars().all()
    return ApiResponse.payload(transform(
        chats,
        ChatTransformer()
    ))
