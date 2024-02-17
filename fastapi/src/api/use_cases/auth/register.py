from src.api.payloads.auth.register import RegisterPayload
from src.database.models.entities.user import User
from src.repository.crud.entities.user import user_repo
from src.utils.crypt import Crypt


class RegisterUseCase:
    @staticmethod
    async def register(payload: RegisterPayload) -> User:
        if await user_repo.get_single(email=payload.email):
            raise Exception('This email is already taken')

        crypt = Crypt()

        hashed_password = crypt.hash(payload.password)
        payload.password = hashed_password

        user = await user_repo.create(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            password=payload.password,
            phone_number=payload.phone_number,
            user_status_id=payload.user_status_id
        )

        return user
