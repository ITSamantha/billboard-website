from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth

router = APIRouter()

connected_users = {}


@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    user = await auth.check_access_token_websocket(websocket)
    connected_users[user.id] = websocket
    while True:
        data = await websocket.receive_text()
        for user_id in connected_users:
            if user_id == user.id:
                continue
            connected_users[user_id].send_text(data)
