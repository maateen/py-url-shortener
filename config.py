SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://shortener:123456@localhost/shortener'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"
DEBUG = True