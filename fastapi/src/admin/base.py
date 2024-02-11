from src.admin.dropdowns.ad_settings_dropdown import advertisement_dropdown
from src.database.session_manager import db_manager
from starlette_admin.contrib.sqla import Admin

admin = Admin(db_manager.engine, title="Otiva Billboard")

admin.add_view(advertisement_dropdown)
