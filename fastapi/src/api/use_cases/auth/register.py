from src.config.jwt.config import settings_jwt
from src.database.models.entities.user import User
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.crypt import Crypt
from src.utils.jwt.jwt_auth import JWT


class RegisterUseCase:
    @staticmethod
    async def register(payload: dict):
        if await SqlAlchemyRepository(db_manager.get_session, User).get_single(email=payload["email"]):
            raise Exception('This email is already taken')

        crypt = Crypt()

        hashed_password = crypt.hash(payload['password'])
        payload['password'] = hashed_password

        user = await SqlAlchemyRepository(db_manager.get_session, User).create(payload)

        jwt = JWT(settings_jwt)
        access_token = jwt.generate_access_token(user.email)
        refresh_token = jwt.generate_refresh_token(user.email)

        return access_token, refresh_token
