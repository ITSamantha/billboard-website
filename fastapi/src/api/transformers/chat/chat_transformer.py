from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.chat.chat_message_transformer import ChatMessageTransformer
from src.api.transformers.user import UserTransformer


class ChatTransformer(BaseTransformer):
    def __init__(self, user_id=None):
        super().__init__()
        self.available_includes = ['messages', "user"]
        self.default_includes = []
        if user_id:
            self.user_id = user_id

    def transform(self, chat):
        return {
            "id": chat.id,
            "created_at": chat.created_at.isoformat()
        }

    def include_messages(self, chat):
        return self.collection(chat.messages, ChatMessageTransformer())

    def include_user(self, chat):
        chat_user = chat.chat_users[0] if chat.chat_users[0].id != self.user_id else chat.chat_users[1]
        return self.item(chat_user.user, UserTransformer())
