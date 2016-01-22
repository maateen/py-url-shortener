from app import db
from app import models
from sys import argv

for arg in argv:
	if arg == 'syncdb':
		db.drop_all()
		db.create_all()