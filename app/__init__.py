from flask import Flask, url_for
from flask_admin import Admin
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask_migrate import Migrate
import sass
import os

app = Flask(__name__)
assets = Environment(app)
admin = Admin(app)
bootstrap = Bootstrap5(app)

from .routes import *