from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
users = []

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users.append(User(id=1, username='Tarun', password='password'))

from routes import *

def __repr__(self):
        return f'<User: {self.username}>'

if(__name__ == '__main__'):
    app.run(debug=True)
