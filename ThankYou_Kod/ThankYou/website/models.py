#Database models
from .import db
from flask_login import UserMixin #UserMixin is used with current_user
from sqlalchemy.sql import func #Automatically adds date

class Note(db.Model): #Table note
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.Date, default=func.now())
    image = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Foreign Key from table 'user' where column is 'id', must be in lower-case

class User(db.Model, UserMixin): #Table user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    user_notes = db.relationship('Note') #Must be in upper-case

class Test(db.Model): 
    id = db.Column(db.Integer, primary_key=True)

