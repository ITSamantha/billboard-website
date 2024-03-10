from fastapi import APIRouter, Depends, Request
from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database.session_manager import db_manager

router = APIRouter(
    prefix="/chats",
)


@router.get("")
async def index(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    chats = request.state.user.chats

    return ApiResponse.payload(chats)
