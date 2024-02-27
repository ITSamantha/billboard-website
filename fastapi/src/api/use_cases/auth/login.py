from src.database.models.entities.user import User
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.crypt import Crypt
from src.utils.jwt.jwt_auth import JWT
from src.api.payloads.auth.login import LoginPayload
from src.config.jwt.config import settings_jwt


class LoginUseCase:
    @staticmethod
    async def login(payload: LoginPayload):
        user = await LoginUseCase.authenticate_user(payload.email, payload.password)
        if not user:
            raise Exception("Incorrect username or password")

        jwt = JWT(settings_jwt)
        access_token = jwt.generate_access_token(payload.email)
        refresh_token = jwt.generate_refresh_token(payload.email)

        return access_token, refresh_token

    @staticmethod
    async def authenticate_user(email: str, password: str):
        user: User = await SqlAlchemyRepository(db_manager.get_session, User).get_single(email=email)
        if not user:
            return False
        crypt = Crypt()
        if not crypt.verify(password, user.password):
            return False
        return user
