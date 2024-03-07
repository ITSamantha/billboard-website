from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth

router = APIRouter(
)


@router.websocket("/ws/echo")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    await websocket.send_text('connected')
    auth.check_access_token()
    await websocket.send_text('checked authenticato')
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
