from datetime import datetime
from datetime import timedelta


def time_ago_in_words(dt):
    now = datetime.now()
    delta = now - dt

    if delta < timedelta(minutes=1):
        return 'just now'
    elif delta < timedelta(hours=1):
        minutes = delta.seconds // 60
        return f'{minutes} minute{"s" if minutes > 1 else ""} ago'
    elif delta < timedelta(days=1):
        hours = delta.seconds // 3600
        return f'{hours} hour{"s" if hours > 1 else ""} ago'
    elif delta < timedelta(weeks=1):
        days = delta.days
        return f'{days} day{"s" if days > 1 else ""} ago'
    elif delta < timedelta(weeks=4):
        weeks = delta.days // 7
        return f'{weeks} week{"s" if weeks > 1 else ""} ago'
    elif delta < timedelta(days=365):
        months = delta.days // 30
        return f'{months} month{"s" if months > 1 else ""} ago'
    else:
        years = delta.days // 365
        return f'{years} year{"s" if years > 1 else ""} ago'


def json_datetime(dt: datetime):
    return dt.strftime('%Y-%m-%d %H:%M:%S') if dt else None
