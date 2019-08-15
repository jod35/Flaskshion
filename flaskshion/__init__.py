from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flaskshion.config import DevConfig
from flask_login import LoginManager
app=Flask(__name__)
app.config.from_object(DevConfig)

db=SQLAlchemy(app)
admin=Admin(app)
login_manager=LoginManager(app)
from flaskshion import views