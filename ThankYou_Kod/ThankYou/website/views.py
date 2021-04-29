from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required #User can only see the home page if they are logged in
def home():
    '''This view returns the home page'''
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1: #If less than one character return an error
            flash('Note is too short!', category='error')
        else: #Else, save note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).all()
    for notes in note:
        print(notes.date)
        print(notes.data)

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
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).all()
    
    test1 = []
    for notes in note:
        x = {
            "startDate": notes.date,
            "endDate": notes.date,
            "summary": notes.data
        }
        test1.append(x)
        y = json.dumps(test1, indent=4, sort_keys=True, default=str)
    # the result is a JSON string:

    return render_template("calendar.html", y=y)
