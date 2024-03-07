from fastapi import WebSocket
from fastapi import APIRouter

router = APIRouter(
    prefix="/ws/chat",
)


@router.websocket("/echo")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
