from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from src.database.models import User
from src.repository.crud.entities.user import user_repo
from src.config.jwt.config import settings_jwt
from src.utils.crypt import Crypt
from src.api.payloads.auth.login import LoginPayload


class LoginUseCase:
    @staticmethod
    async def login(payload: LoginPayload):
        user = await LoginUseCase.authenticate_user(payload.username, payload.password)
        if not user:
            raise Exception("Incorrect username or password")
        data = {
            "sub": payload.username,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=3600)
        }

        access_token = jwt.encode(data, settings_jwt.JWT_SECRET_KEY, algorithm=settings_jwt.JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'token_type': 'bearer'
        }

    @staticmethod
    async def authenticate_user(username: str, password: str):
        user: User = await user_repo.get_single({'username': username})
        if not user:
            return False
        crypt = Crypt()
        if not crypt.verify(password, user['password']):
            return False
        return user
