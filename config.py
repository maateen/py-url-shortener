SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://shortener:123456@localhost/shortener' #Set up your MySQL/MariaDB coonection - mysql+pymysql://username:password@host/database.
SECRET_KEY = "Set a long string that can't be guessed easily"
SQLALCHEMY_ECHO = True #This will show SQLAlchemy output.
SQLALCHEMY_TRACK_MODIFICATIONS = True #This will show SQLAlchemy track modification output.
CSRF_ENABLED = True #Don't make it False.
DEBUG = True #Make it false to turn the debugger off.