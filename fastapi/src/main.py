from fastapi import Request
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware

from src.admin.base import setup_admin
from src.api.responses.api_response import ApiResponse
from src.api.routers import auth, advertisement, review
from src.config.app.config import settings_app
from src.database.session_manager import db_manager


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings_app.APP_NAME,
        debug=settings_app.DEBUG,
        version=settings_app.APP_VERSION
    )

    return application


app = get_application()

admin = setup_admin(app, db_manager.engine)

app.include_router(auth.router)
app.include_router(advertisement.router)
app.include_router(review.router)

# todo: remove
from fastapi import Request
from src.api.responses.api_response import ApiResponse
from src.utils.validator import Validator
from src.utils.validator.exceptions import AppValidationException
@app.post('/test')
async def test(request: Request):
    validator = Validator(await request.json(), {
        'first_name': ['required'],
        'last_name': ['nullable'],
    }, {'first_name': 'kek'})

    validator.validate()

    return ApiResponse.payload({
        'test': 'lol',
        'request': validator.validated(),
    })

@app.exception_handler(AppValidationException)
async def validation_failed(request: Request, exc: AppValidationException):
    return ApiResponse.errors(exc.errors, status_code=422)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return ApiResponse.errors(exc.errors(), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


if __name__ == "__main__":
    uvicorn.run(
        app=settings_app.UVICORN_APP_NAME,
        host=settings_app.UVICORN_HOST,
        port=settings_app.UVICORN_PORT,
        reload=settings_app.UVICORN_RELOAD
    )
