from src.database.models import Country, City, AdStatus, AdType, BookingStatus, BookingType, FilterType, Priority, \
    UserRole, UserStatus, Weekday


def transform_city(city: City) -> dict:
    return {
        "id": city.id,
        "title": city.title
    }


def transform_country(country: Country) -> dict:
    return {
        "id": country.id,
        "title": country.title}


def transform_ad_status(ad_status: AdStatus) -> dict:
    return {
        "id": ad_status.id,
        "title": ad_status.title,
        "is_shown": ad_status.is_shown
    }


def transform_ad_type(ad_type: AdType) -> dict:
    return {
        "id": ad_type.id,
        "title": ad_type.title
    }


def transform_booking_status(booking_status: BookingStatus) -> dict:
    return {
        "id": booking_status.id,
        "title": booking_status.title
    }


def transform_booking_type(booking_type: BookingType) -> dict:
    return {
        "id": booking_type.id,
        "title": booking_type.title
    }


def transform_filter_type(filter_type: FilterType) -> dict:
    return {
        "id": filter_type.id,
        "functional_title": filter_type.functional_title,
        "title": filter_type.title,
        "interval_placeholder_from": filter_type.interval_placeholder_from,
        "interval_placeholder_to": filter_type.interval_placeholder_to
    }


def transform_priority(priority: Priority) -> dict:
    return {
        "id": priority.id,
        "title": priority.title,
        "priority": priority.priority,
        "color": priority.color
    }


def transform_transaction_type(transaction_type: TransactionType) -> dict:
    return {
        "id": transaction_type.id,
        "title": transaction_type.title
    }


def transform_user_role(user_role: UserRole) -> dict:
    return {
        "id": user_role.id,
        "title": user_role.title
    }


def transform_user_status(user_status: UserStatus) -> dict:
    return {
        "id": user_status.id,
        "title": user_status.title,
        "is_available": user_status.is_available
    }


def transform_weekday(weekday: Weekday) -> dict:
    return {
        "id": weekday.id,
        "title": weekday.title,
        "short_title": weekday.short_title,
        "order": weekday.order
    }
