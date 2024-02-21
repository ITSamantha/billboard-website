from sqladmin import Admin

from src.admin.characteristics.ad_status import AdStatusView
from src.admin.entities.advertisment import AdvertisementView


def create_admin_views(admin: Admin):
    admin.add_view(AdStatusView)
    admin.add_view(AdvertisementView)
    return admin


def setup_admin(app, engine):
    admin = create_admin_views(Admin(app, engine, title="Otiva Billboard"))
    return admin
