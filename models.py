from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'