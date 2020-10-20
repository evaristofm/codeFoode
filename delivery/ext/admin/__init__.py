from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView
from delivery.ext.db import db
from delivery.ext.db.models import Category, Items


admin = Admin()

def init_app(app):
    admin.name = "CodeFoods"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Items, db.session))


    