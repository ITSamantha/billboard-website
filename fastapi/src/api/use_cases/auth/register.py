from src.api.payloads.auth.register import RegisterPayload
from src.database.models.entities.user import User
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.crypt import Crypt


class RegisterUseCase:
    @staticmethod
    async def register(payload: RegisterPayload) -> User:
        if await SqlAlchemyRepository(db_manager.get_session, User).get_single(email=payload.email):
            raise Exception('This email is already taken')

        crypt = Crypt()

        hashed_password = crypt.hash(payload.password)
        payload.password = hashed_password

        user = await SqlAlchemyRepository(db_manager.get_session, User).create(payload)

        return user
