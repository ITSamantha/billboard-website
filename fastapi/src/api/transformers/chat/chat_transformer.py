from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.chat.chat_message_transformer import ChatMessageTransformer


class ChatTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = ['messages']

    def transform(self, chat):
        return {
            "id": chat.id,
            "created_at": chat.created_at.isoformat()
        }

    def include_messages(self, chat):
        return self.collection(chat.messages, ChatMessageTransformer())
