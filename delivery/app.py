from flask import Flask, render_template

from delivery.ext import config


"""
    OBS: Tem uma ordem dos inits
    1- APP
    2- CONFIG
    3- DB
    4- MIGRATE
    ...
"""


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    
    # db.init_app(app)
    # auth.init_app(app)
    # admin.init_app(app)
    # migrate.init_app(app)
    # cli.init_app(app)
    # toolbar.init_app(app)
    # site.init_app(app)

    return app