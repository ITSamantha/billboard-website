from src.api.transformers.account.account_transaction_transformer import AccountTransactionTransformer
from src.api.transformers.base_transformer import BaseTransformer


class AccountTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = ['transactions']
        self.default_includes = []

    def transform(self, account):
        return {
            "id": account.id,
            "user_id": account.user_id,
            "balance": account.balance,
            "created_at": account.created_at.isoformat(),
        }

    def include_transactions(self, account):
        return self.collection(account.transactions, AccountTransactionTransformer())
