from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth
from src.utils.redis import redis
from src.utils.pubsub import PubSub


router = APIRouter()
STOPWORD = "STOP"

# todo check that redis pool is created once
# todo share pool between workers
@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    # try:
    #     user = await auth.check_access_token_websocket(websocket)
    # except Exception as e:
    #     await websocket.send_text('Unauthenticated')
    #     await websocket.close()
    #     return

    async for message in PubSub.subscribe('channel:1'):
        await websocket.send_text(message.data)

    await websocket.close()


@router.websocket("/ws/chat/huy")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    await websocket.send_text('type smth')

    await PubSub.publish('channel:1', await websocket.receive_text())

    await websocket.close()
