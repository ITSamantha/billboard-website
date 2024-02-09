from src.utils.jwt.jwt_auth import JWT
from src.config.jwt.config import settings_jwt


class RefreshUseCase:
    @staticmethod
    async def refresh(payload):
        # todo check for revoked
        jwt = JWT(settings_jwt)

        access_token = jwt.generate_access_token(payload['email'])
        refresh_token = jwt.generate_refresh_token(payload['email'])

        return access_token, refresh_token
