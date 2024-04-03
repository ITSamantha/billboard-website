from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.user import UserTransformer


class ChatUserTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = []

    def transform(self, chat_message):
        return {
            "id": chat_message.id,
            "chat_id": chat_message.chat_id,
            "user_id": chat_message.user_id,
        }

    def include_user(self, chat):
        return self.item(chat.user, UserTransformer())
