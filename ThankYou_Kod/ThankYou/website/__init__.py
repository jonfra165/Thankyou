from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

db = SQLAlchemy()
db_name = "test_database" #Database name


try: #Create database
    conn = pyodbc.connect("driver={SQL Server};server=localhost; database=master; trusted_connection=true", autocommit=True) 
    cursor = conn.cursor()
    cursor.execute(f'CREATE DATABASE {db_name};')

    print(f'Database {db_name} created!')
except: #SQL ASK Anton or someone else
    def create_database(app):
        db.create_all(app = app)

def create_app():
    app = Flask(__name__) #Initialize flask 
    app.config['SECRET_KEY'] = 'CHOSEN_KEY' #Encrypt/secure cookies and data related to our session

    app.config["SQLALCHEMY_DATABASE_URI"] = f'mssql+pyodbc://localhost/{db_name}?driver=SQL+Server?trusted_connection=yes' #No idea what to comment and what it does
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
