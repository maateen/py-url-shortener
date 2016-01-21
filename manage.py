from sys import argv
from app import db
from app import models

for arg in argv:
	if arg == 'syncdb':
		db.create_all()