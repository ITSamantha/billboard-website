from src.api.payloads.base import BasePayload


class AdvertisementAdTag(BasePayload):
    advertisement_id: int
    ad_tag_id: int
