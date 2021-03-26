from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__) #Initialize flask 
    app.config['SECRET_KEY'] = 'CHOSEN_KEY' #Encrypt/secure cookies and data related to our session
 
    from .views import views #From views.py
    from .auth import auth #From auth.py

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app