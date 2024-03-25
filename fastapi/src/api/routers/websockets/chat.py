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

    # channel_name = f"user_{user.id}"
    channel_name = f"user_1"
    while True:
        redis_connection = redis.get_connection()
        # Subscribe to channel
        channel, = await redis_connection.subscribe(channel_name)
        try:
            while await channel.wait_message():
                message = await channel.get(encoding='utf-8')
                await websocket.send_text(message)
        finally:
            await channel.unsubscribe(channel_name)

@router.websocket("/ws/chat/huy")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    await websocket.send_text('type smth')
    msg = await websocket.receive_text()
    channel_name = 'user_1'
    redis_connection = redis.get_connection()
    await redis_connection.publish(channel_name, msg)

