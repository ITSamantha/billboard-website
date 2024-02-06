import uvicorn
from fastapi import FastAPI
from src.config.app.config import settings_app
from routers import auth


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings_app.APP_NAME,
        debug=settings_app.DEBUG,
        version=settings_app.APP_VERSION
    )

    return application


app = get_application()

app.include_router(auth.router) 


if __name__ == "__main__":
    uvicorn.run(
        app=settings_app.UVICORN_APP_NAME,
        host=settings_app.UVICORN_HOST,
        port=settings_app.UVICORN_PORT,
        reload=settings_app.UVICORN_RELOAD
    )
