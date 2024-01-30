import datetime


class AdBookingAvailable:
    id: int
    advertisement_id: int
    time_from: datetime.datetime
    time_end: datetime.datetime
    min_booking_time: datetime.datetime
    max_booking_time: datetime.datetime
    price: float
