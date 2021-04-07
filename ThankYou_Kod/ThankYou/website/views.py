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
        note = request.form.get('note')

        if len(note) < 1: #If less than one character return an error
            flash('Note is too short!', category='error')
        else: #Else, save note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    user = current_user.id 
    note = Note.query.all() #get all values from table Note
    
    return render_template('home.html', user=user, note=note)

