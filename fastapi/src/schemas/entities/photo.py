from pydantic import BaseModel


class Photo(BaseModel):
    photo_path: str
    photo_thumb: str


def create_photo(photo):
    pass


class PhotoResponse(Photo, BaseResponseSchema):
    pass


class PhotoCreate(Photo):
    pass


class PhotoUpdate(Photo):
    pass
