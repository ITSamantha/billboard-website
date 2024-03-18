from fastapi import FastAPI

from src.api.routers import auth, advertisement, review, category, chat

from src.api.routers.location import location
from src.api.routers.websockets import chat as ws_chat


def create_app_routers(app: FastAPI):
    app.include_router(auth.router)
    app.include_router(advertisement.router)
    app.include_router(review.router)
    app.include_router(category.router)
    app.include_router(location.router)
    app.include_router(ws_chat.router)
    app.include_router(chat.router)
    return app
