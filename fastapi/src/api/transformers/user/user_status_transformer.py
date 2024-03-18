from src.api.transformers.base_transformer import BaseTransformer


class UserStatusTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, user_status):
        return {
            "id": user_status.id,
            "title": user_status.title,
            "is_available": user_status.is_available
        }
