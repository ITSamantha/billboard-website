from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth
from src.utils.jwt.token_type import TokenType

router = APIRouter(
)


@router.websocket("/ws/echo")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    await websocket.send_text('connected')
    token = await websocket.receive_text()
    _, user = auth.check_token(token, TokenType.ACCESS)
    await websocket.send_text('checked authenticato')
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
