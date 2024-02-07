import uvicorn
from fastapi import FastAPI
from sqladmin import Admin, ModelView

from src.config.app.config import settings_app
from src.api.routes import auth, ad_status
from src.database.session_manager import db_manager
from src.database.models import AdStatus


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings_app.APP_NAME,
        debug=settings_app.DEBUG,
        version=settings_app.APP_VERSION
    )

    return application


app = get_application()
admin = Admin(app, db_manager.engine)

app.include_router(auth.router)
app.include_router(ad_status.router)


class AdStatusAdmin(ModelView, model=AdStatus):
    pass


admin.add_view(AdStatusAdmin)

if __name__ == "__main__":
    uvicorn.run(
        app=settings_app.UVICORN_APP_NAME,
        host=settings_app.UVICORN_HOST,
        port=settings_app.UVICORN_PORT,
        reload=settings_app.UVICORN_RELOAD
    )
