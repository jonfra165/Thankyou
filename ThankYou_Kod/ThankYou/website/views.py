from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required #User can only see the home page if they are logged in
def home():
    '''This view returns the home page'''
    if request.method == 'POST':
        note = request.form.get('note') #Get note from home.html

        if len(note) < 1: #If less than one character return an error
            flash('Note is too short!', category='error')
        else: #Else, save note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success') 
    
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).all() #Problemet?
    
    return render_template('home.html', user=user, note=note)

@views.route("/profile")
@login_required #User can only see the profile page if they are logged in
def profile():
    ''' This view returns the profile page '''
    user = current_user
    return render_template("profile.html", user=user)

@views.route("/calendar")
@login_required
def calendar():
    user = current_user
    return render_template("calendar.html", user=user)

def get_date():
    '''1 parameter som är ett datum, sen ska funktionen hämta från databasen alla posts som finns på det datumet och skriva ut det i json format
    Skicka tillbaka i json'''

    test_user = current_user.id 
    test_note = Note.query.filter_by(user_id=user).all()
    test_note = list(test_note)

    return render_template('home.html', test_user=test_user, test_note=test_note)

    #Hämta all datum och tillhörande anteckningar
    #Sparar det i json
    #Skickar till html.fil
