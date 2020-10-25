from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

udb = SQLAlchemy(app) # users database
users = []

if __name__ == '__main__':
    app.run(debug=True)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users.append(User(id=1, username='Tarun', password='password'))