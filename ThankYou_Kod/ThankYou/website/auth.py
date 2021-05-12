#Authentication
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note #import user table
from werkzeug.security import generate_password_hash, check_password_hash #Hash for password
from . import db #import database "cursor"
from flask_login import login_user, login_required, logout_user, current_user
from validate_email import validate_email

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''This is the user login'''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first() #Checks row in table if email exists

        if user: #If email has a row
            if check_password_hash(user.password, password): #If email has a row and correct password
                flash('Logged in succesfully!', category='success')
                login_user(user, remember=True) #Remembers that user is logged in
                return redirect(url_for('views.home')) #Redirect to home page
            else: #Incorrect password
                flash('Incorrect password, try again', category='error')
        else: #If email doesn't have a row in the table then it does not exist
            flash('Email doesn\’t  exist!', category='error')

    return render_template('login.html')  
            
@auth.route('/logout')
@login_required #Requires that user is logged in to be able to log out
def logout():
    '''This is the user logout'''
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''This is a sign-up form which asks the user for their email, first name and password'''
    if request.method == 'POST':
        email = request.form.get('email') 
        fname = request.form.get('fname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        validate = validate_email(email)
        print(email)
    
        user = User.query.filter_by(email=email).first()
        if user: 
            flash('Email already exists!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif validate == False: 
            flash('This email does not exist', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters.', category='error')
        elif not any(p.isupper() for p in password1): # Check if password includes at least one capital letter 
            flash('Password must include at least one capital letter.', category='error')
        elif not any(p.isdigit() for p in password1): # Check if password includes at least one number 
            flash('Password must include at least one number.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif not any(char.isupper() for char in password1):
            flash('Password should have at least one uppercase letter', category='error')
        elif not any(char.isdigit() for char in password1):
            flash('Password should have at least one numeral', category='error')
        else: #Insert new user to database
            new_user = User(email=email, first_name=fname, password=generate_password_hash(password1, method='sha256')) #Hash password
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) #Remembers that user is logged in
            flash('Account created', category='sucess')

            return redirect(url_for('views.home')) #Redirect to login page
            
    return render_template("sign_up.html")
