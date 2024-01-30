from __future__ import annotations

import datetime


class Booking:
    advertisement_id: int
    user_id: int
    time_from: datetime.datetime
    time_end: datetime.datetime
    booking_status_id: int
    guest_count: int | None

    deadline_at: datetime.datetime

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime


# [{
#   from: 12.01.2024 12:00,
#   to: 16.01.2024 15:00
# }, { ... }]