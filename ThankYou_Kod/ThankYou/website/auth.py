#Authentication
from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''This is the user login'''
    data = request.form
    print(data)
    return render_template('login.html')  

    #return render_template('home.html') [to be implemented later]       

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

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters.', category='error')
        else:
            flash('Account created', category='sucess')
            return redirect(url_for('auth.login')) #REDIRECT TO LOGIN PAGE
            
    return render_template("sign_up.html")