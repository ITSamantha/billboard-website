from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.chat.chat_user_transformer import ChatUserTransformer


class ChatMessageTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = ['chat_user']

    def transform(self, chat):
        return {
            "id": chat.id,
            "text": chat.text,
            "created_at": chat.created_at,
            "seen_at": chat.seen_at,
        }

    def include_chat_user(self, chat):
        return self.item(chat.chat_user, ChatUserTransformer())
