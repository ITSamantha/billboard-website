from src.api.payloads.auth.register import RegisterPayload
from src.database.models.entities.user import User
from src.repository.crud.entities.user import user_repo


class RegisterUseCase:
    @staticmethod
    async def register(payload: RegisterPayload) -> User:
        raise NotImplementedError
