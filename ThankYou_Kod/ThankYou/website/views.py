from flask import Blueprint, render_template, url_for, redirect

views = Blueprint('views', __name__)

@views.route('/')
def sign_up():
    '''This view redirects to the sign up page'''
    return redirect(url_for('auth.sign_up'))

@views.route('/home')
def home():
    '''This view returns the home page'''
    return render_template('home.html')