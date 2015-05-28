from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#use config file
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views