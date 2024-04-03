from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.chat.chat_user_transformer import ChatUserTransformer


class ChatMessageTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = ['chat_user']

    def transform(self, chat_message):
        return {
            "id": chat_message.id,
            "chat_id": chat_message.chat_id,
            "text": chat_message.text,
            "created_at": chat_message.created_at.isoformat(),
            "seen_at": chat_message.seen_at.isoformat() if chat_message.seen_at else None,
        }

    def include_chat_user(self, chat_message):
        return self.item(chat_message.chat_user, ChatUserTransformer())
