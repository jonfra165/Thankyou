#Authentication
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import user #import user table
from werkzeug.security import generate_password_hash, check_password_hash #Hash for password
from . import db #import database "cursor"
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''This is the user login'''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_login = user.query.filter_by(email=email).first() #Checks row in table if email exists

        if user: #If email has a row
            if check_password_hash(user_login.password, password): #If email has a row and correct password
                flash('Logged in succesfully!', category='success')
                return redirect(url_for('views.home')) #Redirect to home page
            else: #Incorrect password
                flash('Incorrect password, try again', category='error')
        else: #If email doesn't have a row in the table then it does not exist
            flash('Email does\'nt exist!', category='error')

    return render_template('login.html')  
            
@auth.route('/logout')
def logout():
    '''This is the user logout'''
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''This is a sign-up form which asks the user for their email, first name and password'''

    if request.method == 'POST':
        email = request.form.get('email') 
        fname = request.form.get('fname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_sign_up = user.query.filter_by(email=email).first()
        if user: 
            flash('Email already exists!', category='error')
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters.', category='error')
        else: #Insert new user to database
            new_user = user(email=email, first_name=fname, password=generate_password_hash(password1, method='sha256')) #Hash password
            db.session.add(new_user)
            db.session.commit()

            flash('Account created', category='sucess')
 
            return redirect(url_for('auth.login')) #Redirect to login page
            
    return render_template("sign_up.html")