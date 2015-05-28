from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
#use config file
app.config.from_object('config')
#DataBase
db = SQLAlchemy(app)
#Login
lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

from app import views