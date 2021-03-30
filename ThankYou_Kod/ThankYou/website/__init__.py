from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import mysql.connector as mariadb
import pymysql

db = SQLAlchemy()
db_name = "testdb" #Database name

#db = SQLAlchemy()
#DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #Initialize flask 
    app.config['SECRET_KEY'] = 'CHOSEN_KEY' #Encrypt/secure cookies and data related to our session

    app.config["SQLALCHEMY_DATABASE_URI"] = f'mariadb+pymysql://root:password@localhost/{db_name}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Causes an error if not included
    db.init_app(app) #Initiate db

    #Routes
    from .views import views #From views.py
    from .auth import auth #From auth.py

    #Database tables
    from .models import user

    #Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #No clue, ask Anton or someone else
    create_database(app)

    return app

def create_database(app):
    db.create_all(app = app)