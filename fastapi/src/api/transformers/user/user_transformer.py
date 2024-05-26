from src.api.transformers.base_transformer import BaseTransformer
from src.api.transformers.user.user_status_transformer import UserStatusTransformer
from src.utils.time import json_datetime, time_ago_in_words


class UserTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()
        self.available_includes = ["advertisements",
                                   "ad_favourites"]
        self.default_includes = [
            'user_status'
        ]

    def transform(self, user):
        return {
            "id": user.id,
            "avatar_id": user.avatar.id if user.avatar else None,
            "avatar": user.avatar.link if user.avatar else None,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "email_verified_at": json_datetime(user.email_verified_at),
            "phone_verified_at": json_datetime(user.phone_verified_at),
            "phone_number": user.phone_number,
            "available_ads": user.available_ads,
            "created_at": json_datetime(user.created_at),
            "created_at_str": time_ago_in_words(user.created_at),
            "updated_at": json_datetime(user.updated_at),
            "updated_at_str": time_ago_in_words(user.updated_at),
            "deleted_at": json_datetime(user.deleted_at)
        }

    def include_user_status(self, user):
        return self.item(user.user_status, UserStatusTransformer())

    def include_advertisements(self, user):
        from src.api.transformers.advertisement.advertisement_transformer import AdvertisementTransformer
        return self.collection(user.advertisements, AdvertisementTransformer().include(['ad_photos']))

    def include_ad_favourites(self, user):
        from src.api.transformers.advertisement.advertisement_transformer import AdvertisementTransformer
        return self.collection([ad.advertisement for ad in user.ad_favourites], AdvertisementTransformer())
