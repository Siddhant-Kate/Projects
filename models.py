from app import udb

class Users(udb.Model):
    id = udb.Column(udb.Integer, primary_key=True)
    name = udb.Column(udb.String(255), nullable=False)
    
