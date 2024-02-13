from sqladmin import Admin

from src.admin.characteristics.ad_status import AdStatusView


def setup_admin(app, engine):
    admin = Admin(app, engine, title="Otiva Billboard")
    admin.add_view(AdStatusView)
    return admin


"""
admin.add_view(advertisement_dropdown)
admin.add_view(booking_dropdown)
admin.add_view(user_dropdown)
admin.add_view(location_dropdown)
"""
