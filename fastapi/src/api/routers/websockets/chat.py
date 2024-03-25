from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth

router = APIRouter()

connected_users = {}


@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    try:
        user = await auth.check_access_token_websocket(websocket)
    except Exception as e:
        await websocket.send('Unauthenticated')
        await websocket.close()
        return

    connected_users[user.id] = websocket
    while True:
        # await websocket.send_text(str(len(connected_users)))
        # await websocket.send_text('uesr_id: ' + str(user.id))
        data = await websocket.receive_text()
        for user_id in connected_users:
            if user_id == user.id:
                continue
            connected_users[user_id].send_text(data)
