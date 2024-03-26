from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth
from src.utils.pubsub import PubSub


router = APIRouter()


# todo check that redis pool is created once
# todo share pool between workers
@router.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    try:
        user = await auth.check_access_token_websocket(websocket)
    except Exception as e:
        await websocket.send_text('Unauthenticated')
        await websocket.close()
        return

    channel_name = f'notifications:{user.id}'

    async for message in PubSub.subscribe(channel_name):
        await websocket.send_text(message.data)

    await websocket.close()
