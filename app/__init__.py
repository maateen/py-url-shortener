from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# We have initialized our app as an instance of Flask class imported
# above. The first argument is the name of the application’s module or
# package.

app.config.from_object('config')
# This loads the configuration from config.py

db = SQLAlchemy(app)
# We have initialized our db as an instance of SQLAlchemy class imported
# above. The arguement we have passed actually making the connection
# between our app and database.

from app import api
# This line will import all codes writing in api.py. We have imported this
# here due to overcome circular import error.

from app import views
# This line will import all codes writing in views.py. We have imported
# this here due to overcome circular import error.
