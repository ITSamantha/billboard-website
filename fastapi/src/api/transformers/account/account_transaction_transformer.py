from src.api.transformers.account.account_transaction_type_transformer import AccountTransactionTypeTransformer
from src.api.transformers.base_transformer import BaseTransformer


class AccountTransactionTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = []
        self.default_includes = ['type']

    def transform(self, transaction):
        return {
            "id": transaction.id,
            "account_id": transaction.account_id,
            "amount": transaction.amount,
            "created_at": transaction.created_at.isoformat(),
        }

    def include_type(self, transaction):
        return self.item(transaction.type, AccountTransactionTypeTransformer())
