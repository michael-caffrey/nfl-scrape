from flask import Flask
import os

app = Flask(__name__)

env = os.environ
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{env['DB_USERNAME']}:{env['DB_PASSWORD']}@{env['DB_HOST']}:{env['DB_PORT']}/{env['DB_NAME']}"

from backend.models import db
db.app = app
db.init_app(app)

import backend.controllers
