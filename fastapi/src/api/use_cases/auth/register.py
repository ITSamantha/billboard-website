from src.api.payloads.auth.register import RegisterPayload
from src.database.models.entities.user import User
from src.repository.crud.entities.user import user_repo
from src.utils.crypt import Crypt


class RegisterUseCase:
    @staticmethod
    def register(payload: RegisterPayload) -> User:
        if await user_repo.get_single(email=payload.email):
            raise Exception('This email is already taken')

        crypt = Crypt()
        hashed_password = crypt.hash(payload.password)

        user = await user_repo.create({
            'user_name': payload.user_name,
            'email': payload.email,
            'password': hashed_password,
            'phone_number': payload.phone_number,
            'user_status_id': payload.user_status_id,
        })

        return user
