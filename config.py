SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@host/database'
# The database URI that should be used for the connection. Examples:
# mysql+pymysql://username:password@host/database.

SECRET_KEY = "Set a long string that can't be guessed easily"

SQLALCHEMY_ECHO = True
# If set to True SQLAlchemy will log all the statements issued to stderr
# which can be useful for debugging.

SQLALCHEMY_TRACK_MODIFICATIONS = True
# If set to True, Flask-SQLAlchemy will track modifications of objects and
# emit signals. The default is None, which enables tracking but issues a
# warning that it will be disabled by default in the future. This requires
# extra memory and should be disabled if not needed.

WTF_CSRF_ENABLED = True
# Disable/enable CSRF protection for forms. Default is True.

DEBUG = True
# It enables/disables debug mode. If True, then debug mode is enabled
# while False means that debug mode is disabled. Make it False when
# deploying to production server.
