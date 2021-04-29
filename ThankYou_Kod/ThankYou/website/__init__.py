from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
import mysql.connector as mariadb
import pymysql

db = SQLAlchemy() #Cursor
db_name = "testdb" #Database name

def create_app():
    app = Flask(__name__) #Initialize flask 
    app.config['SECRET_KEY'] = 'CHOSEN_KEY' #Encrypt/secure cookies and data related to our session

    app.config["SQLALCHEMY_DATABASE_URI"] = f'mariadb+pymysql://root:password@localhost/{db_name}' #Connects to database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Causes an error if not included
    db.init_app(app) #Initiate db

    #Routes
    from .views import views #From views.py
    from .auth import auth #From auth.py

    #Database tables
    from .models import User, Note 

    #Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    #Connect to MariaDB
    sqlalchemy_mariadb(app)

    #Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #If logger is not logged in, show login page
    login_manager.init_app(app) #Telling Login Manager which app we are using

    @login_manager.user_loader
    def load_user(id):
        '''Telling flask how we load a user'''
        return User.query.get(int(id))

    return app

def sqlalchemy_mariadb(app):
    '''Connects SQLAlchemy to MariaDB to edit database through code'''
    db.create_all(app=app)
