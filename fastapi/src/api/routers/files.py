from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.api.responses.api_response import ApiResponse
from src.config.app.config import settings_app

router = APIRouter(
    prefix="/files",
    tags=["files"],
)


@router.get('/{disk}/{path}')
async def get_file(path: str, disk: str):
    try:
        image_path = settings_app.APP_PATH + '/storage/' + disk + '/' + path
        return FileResponse(image_path)
    except Exception as e:
        return ApiResponse.error(str(e))
