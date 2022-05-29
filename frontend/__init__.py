from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
admin = Admin(app)
bootstrap = Bootstrap5(app)