from app import db
from flask_sqlalchemy import SQLAlchemy


class Urls(db.Model):
    # We are declaring models.

    __tablename__ = 'urls'
    id = db.Column(db.BigInteger, primary_key=True)
    short_url = db.Column(db.String(100))
    long_url = db.Column(db.Text)

    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url
