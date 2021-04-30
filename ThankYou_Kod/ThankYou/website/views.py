from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import requests
import re
import json

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


    response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en')
    quote_author = response.text

    if "(" not in quote_author:
        print("Cannot accept quote")
    else:
        print(quote_author)

    quote_author_list = quote_author.replace('(', '').replace(')', '').split(".")
    quote = quote_author_list
    
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).all()
    for notes in note:
        print(notes.date)
        print(notes.data)

    return render_template('home.html', user=user, note=note, quote=quote)

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
    
    note_list = []
    for notes in note:
        x = {
            "startDate": notes.date,
            "endDate": notes.date,
            "summary": notes.data
        }
        note_list.append(x)

        y = json.dumps(note_list, indent=4, sort_keys=True, default=str) # The result is a JSON string:


    json_note = re.sub(r'(?<!: )"(\S*?)"', '\\1', y) #Remove quotation marks from dictionary keys

    print(json_note)

    return render_template("calendar.html", json_note=json_note)
