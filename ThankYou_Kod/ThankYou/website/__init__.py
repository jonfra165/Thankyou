from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
#DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #Initialize flask 
    app.config['SECRET_KEY'] = 'CHOSEN_KEY' #Encrypt/secure cookies and data related to our session
    
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://MySQLServerName/{DB_NAME}?driver=SQL+Server?trusted_connection=yes'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #db.init_app(app)

 
    from .views import views #From views.py
    from .auth import auth #From auth.py

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app