from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database.session_manager import db_manager
from sqlalchemy.orm import joinedload
from src.database.models.entities.user import User
from src.database.models.entities.chat_user import ChatUser
from src.database.models.entities.chat import Chat

router = APIRouter(
    prefix="/chats",
)


@router.get("")
async def index(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    async with db_manager.get_session() as session:
        user = session.query(User).options(
            joinedload(User.chat_users)
            .subqueryload(ChatUser.chat)
            .subqueryload(Chat.messages)
        ).get(request.state.user.id)

    return ApiResponse.payload(user.chats)
