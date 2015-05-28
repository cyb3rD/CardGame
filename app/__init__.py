from flask import Flask

app = Flask(__name__)
#use config file
app.config.from_object('config')

from app import views