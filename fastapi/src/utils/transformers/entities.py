from src.database.models import Advertisement, Address, City, Country, AdTag, Category, Review, User
from src.utils.time import time_ago_in_words, json_datetime
from src.utils.transformers.characteristics import transform_country, transform_city, transform_ad_type, \
    transform_ad_status, transform_user_status


def transform_ad_tag(ad_tag: AdTag) -> dict:
    return {
        "id": ad_tag.id,
        "title": ad_tag.title
    }


def transform_user(user: User) -> dict:
    return {
        "id": user.id,
        "avatar": "avatar",  # transform_avatar(user.avatar) if user.avatar else None,
        "user_status": transform_user_status(user.user_status) if user.user_status else None,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "email_verified_at": json_datetime(user.email_verified_at),
        "phone_verified_at": json_datetime(user.phone_verified_at),
        "phone_number": user.phone_number,
        "created_at": json_datetime(user.created_at),
        "created_at_str": time_ago_in_words(user.created_at),
        "updated_at": json_datetime(user.updated_at),
        "updated_at_str": time_ago_in_words(user.updated_at),
        "deleted_at": json_datetime(user.deleted_at)
    }


def transform_category(category: Category) -> dict:
    return {
        "id": category.id,
        "title": category.title,
        "order": category.order,
        "bookable": category.bookable,
        "url": category.url,
        "map_addressable": category.map_addressable,
        "meta_title": category.meta_title,
        "meta_description": category.meta_description,
        "parent_id": category.parent_id
        # parent object
    }


def transform_review(review: Review) -> dict:
    return {
        "id": review.id,
        "rating": review.rating,
        "text": review.text,
        "advertisement_id": review.advertisement_id,
        "user": transform_user(review.user) if review.user else None,
        "created_at": json_datetime(review.created_at),
        "created_at_str": time_ago_in_words(review.created_at),
        "updated_at": json_datetime(review.updated_at),
        "updated_at_str": time_ago_in_words(review.updated_at),
        "deleted_at": json_datetime(review.deleted_at)
    }


def transform_ad_photo():
    return "photo"


def transform_advertisement(advertisement: Advertisement) -> dict:
    # TODO:  transform RELATION ATTRS HERE AS IN MODEL
    return {"id": advertisement.id,
            "title": advertisement.title,
            "user_description": advertisement.user_description,
            "address": transform_address(advertisement.address) if advertisement.address else None,
            "user": transform_user(advertisement.user) if advertisement.user else None,
            "ad_status": transform_ad_status(advertisement.ad_status) if advertisement.ad_status else None,
            "ad_type": transform_ad_type(advertisement.ad_type) if advertisement.ad_type else None,
            "ad_tags": [transform_ad_tag(tag) for tag in advertisement.ad_tags] if advertisement.ad_tags else None,
            "ad_photos": [transform_ad_photo(photo) for photo in
                          advertisement.ad_photos] if advertisement.ad_photos else None,
            "category": transform_category(advertisement.category),
            "reviews": [transform_review(review) for review in advertisement.reviews if
                        not review.deleted_at] if advertisement.reviews else None,
            "price": advertisement.price,
            "bookable": advertisement.category.bookable,
            "created_at": json_datetime(advertisement.created_at),
            "created_at_str": time_ago_in_words(advertisement.created_at) if advertisement.created_at else None,
            "updated_at": json_datetime(advertisement.updated_at),
            "updated_at_str": time_ago_in_words(advertisement.updated_at) if advertisement.updated_at else None,
            "deleted_at": json_datetime(advertisement.deleted_at)
            }


def transform_address(address: Address) -> dict:
    return {
        "id": address.id,
        "country": transform_country(address.country) if address.country else None,
        "city": transform_city(address.city) if address.city else None,
        "street": address.street,
        "house": address.house,
        "flat": address.flat,
        "longitude": address.longitude,
        "latitude": address.latitude
    }
