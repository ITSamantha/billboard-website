from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.user.user_status_transformer import UserStatusTransformer
from src.utils.time import json_datetime, time_ago_in_words


class UserTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = [
            'user_status',
        ]

    def transform(self, user):
        return {
            "id": user.id,
            "avatar": "avatar",
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "email_verified_at": json_datetime(user.email_verified_at),
            "phone_verified_at": json_datetime(user.phone_verified_at),
            "phone_number": user.phone_number,
            "created_at": json_datetime(user.created_at),
            "created_at_str": time_ago_in_words(user.created_at),
            "updated_at": json_datetime(user.updated_at),
            "updated_at_str": time_ago_in_words(user.updated_at),
            "deleted_at": json_datetime(user.deleted_at)
        }

    def include_user_status(self, user):
        return self.item(user.user_status, UserStatusTransformer())
