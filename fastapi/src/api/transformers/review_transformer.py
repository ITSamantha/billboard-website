from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.user import UserTransformer
from src.utils.time import json_datetime, time_ago_in_words


class ReviewTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = [
            'user',
        ]
        self.default_includes = []

    def transform(self, review):
        return {
            "id": review.id,
            "rating": review.rating,
            "text": review.text,
            "advertisement_id": review.advertisement_id,
            "created_at": json_datetime(review.created_at),
            "created_at_str": time_ago_in_words(review.created_at),
            "updated_at": json_datetime(review.updated_at),
            "updated_at_str": time_ago_in_words(review.updated_at),
            "deleted_at": json_datetime(review.deleted_at)
        }
    
    def include_user(self, review):
        return self.item(review.user, UserTransformer())
