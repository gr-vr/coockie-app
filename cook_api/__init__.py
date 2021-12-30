
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from cook_api.config import Settings


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = Settings.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
