from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth
from src.utils.redis import redis

router = APIRouter()


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

    channel_name = f"user_1"
    redis_connection = redis.get_connection()
    psub = redis_connection.pubsub()
    async with psub as p:
        await p.subscribe("channel:1")
        import json
        try:
            while True:
                msg = await p.get_message()
                await websocket.send_text(json.dumps(msg))
        finally:
            await p.unsubscribe(channel_name)


@router.websocket("/ws/chat/huy")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    await websocket.send_text('type smth')
    msg = await websocket.receive_text()
    channel_name = f"user_1"
    redis_connection = redis.get_connection()
    await redis_connection.publish(channel_name, msg)
    await redis_connection.close()
