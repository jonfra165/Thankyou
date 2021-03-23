from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")            

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''Förklaring'''
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
            return redirect(url_for('views.home'))
            
    return render_template("sign_up.html")