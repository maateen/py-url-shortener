from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)