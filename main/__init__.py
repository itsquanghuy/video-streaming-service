from importlib import import_module

from flask import Flask
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .commons.error_handlers import register_error_handlers
from .config import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
basic_auth = BasicAuth(app)

CORS(app)


def register_subpackages():
    from main import models

    for m in models.__all__:
        import_module("main.models." + m)

    import main.admin
    import main.controllers  # noqa


register_subpackages()
register_error_handlers(app)
