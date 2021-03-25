from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    '''This view returns home page'''
    return render_template("home.html")