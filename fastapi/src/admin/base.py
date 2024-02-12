from src.admin.dropdowns import advertisement_dropdown, booking_dropdown, user_dropdown, location_dropdown

from src.database.session_manager import db_manager
from starlette_admin.contrib.sqla import Admin

admin = Admin(db_manager.engine, title="Otiva Billboard")

admin.add_view(advertisement_dropdown)
admin.add_view(booking_dropdown)
admin.add_view(user_dropdown)
admin.add_view(location_dropdown)
