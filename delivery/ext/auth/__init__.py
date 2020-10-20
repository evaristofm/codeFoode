from delivery.ext.auth import models # noqa

from delivery.ext.db import db
from delivery.ext.admin import admin as main_admin
from delivery.ext.auth.models import User
from delivery.ext.auth.admin import UserAdmin


def init_app(app):
    
    main_admin.add_view(UserAdmin(User, db.session))