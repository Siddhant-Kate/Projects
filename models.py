from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, nullable = False)
    username = db.Column(db.String(100), nullable = False, primary_key = True)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'Username :{self.username} created with email id: {self.email}'