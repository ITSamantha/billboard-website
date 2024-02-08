from fastapi import Request, HTTPException
from jose import JWTError, jwt

from src.config.jwt.config import settings_jwt
from src.repository.crud.entities.user import user_repo


class IsAuthenticated:
    async def __call__(self, request: Request):
        access_token = request.cookies.get('jwt')

        credentials_exception = HTTPException(
            status_code=401,
            detail="Unauthenticated",
        )
        try:
            payload = jwt.decode(access_token, settings_jwt.JWT_SECRET_KEY, algorithm=settings_jwt.JWT_ALGORITHM)
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = await user_repo.get_single(email=email)
        if user is None:
            raise credentials_exception
        return user
