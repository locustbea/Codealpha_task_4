from flask_sqlalchemy import SQLAlchemy
import string
import random

db = SQLAlchemy()

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(10), unique=True)

    def __init__(self, original_url, short_url=None):
        self.original_url = original_url
        self.short_url = short_url or self.generate_short_url()

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for _ in range(6))
            if not URLMap.query.filter_by(short_url=short_url).first():
                return short_url
