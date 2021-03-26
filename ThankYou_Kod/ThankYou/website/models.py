#Database models
from . import db
from flask_login import UserMixin

class user(db.Model, UserMixin): #Table user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
