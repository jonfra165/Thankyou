from flask import Blueprint, render_template, url_for, redirect, request, flash, Flask, send_from_directory
from flask_login import login_required, current_user
from .models import Note
from . import db
import requests
import re
import json
import os
from werkzeug.utils import secure_filename
views = Blueprint('views', __name__)

UPLOAD_FOLDER = 'ThankYou_Kod/ThankYou/website/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
@views.route('/', methods=['GET', 'POST'])
@login_required #User can only see the home page if they are logged in
def home():
    '''This view returns the home page'''
    response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en')
    quote_str = response.text
    quote_list = quote_str.split('(')

    quote = quote_list[0]
    if quote_list[1] != '':
        author = quote_list[1].replace(')', '')
    else:
        author = 'Anonymous'

    user = current_user.id 
    note = Note.query.filter_by(user_id=user).all()

    if request.method == 'POST':
        note1 = request.form.get('note1')
        note2 = request.form.get('note2')
        note3 = request.form.get('note3')
        # check if the post request has the file part
    
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        # if user does not select file, browser also
        # submit an empty part without filename

        new_note1 = ''
        if note1 != '' or file1.filename != '' :
            if file1.filename != '' and allowed_file(file1.filename):
                filepath1 = os.path.join("/static/uploads", secure_filename(file1.filename))
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file1.filename)))
                if note1 != '' :
                    new_note1 = Note(data=note1, image=filepath1, user_id=current_user.id)
                else:
                    new_note1 = Note(image=filepath1, user_id=current_user.id)
            elif note1 != '' :
                new_note1 = Note(data=note1, user_id=current_user.id)
        else:
            flash('Please add eather a Note or an Image to each post! (post 1)', category='error')
            return render_template('home.html', user=user, note=note, quote=quote, author=author)

        new_note2 = ''
        if note2 != '' or file2.filename != '' :
            if file2.filename != '' and allowed_file(file2.filename):
                filepath2 = os.path.join("/static/uploads", secure_filename(file2.filename))
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))
                if note2 != '' :
                    new_note2 = Note(data=note2, image=filepath2, user_id=current_user.id)
                else:
                    new_note2 = Note(image=filepath2, user_id=current_user.id)
            elif note2 != '' :
                new_note2 = Note(data=note2, user_id=current_user.id)
        else:
            flash('Please add eather a Note or an Image to each post! (post 2)', category='error')
            return render_template('home.html', user=user, note=note, quote=quote, author=author)

        new_note3 = ''
        if note3 != '' or file3.filename != '' :
            if file3.filename != '' and allowed_file(file3.filename):
                filepath3 = os.path.join("/static/uploads", secure_filename(file3.filename))
                file3.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file3.filename)))
                if note3 != '' :
                    new_note3 = Note(data=note3, image=filepath3, user_id=current_user.id)
                else:
                    new_note3 = Note(image=filepath3, user_id=current_user.id)
            elif note3 != '' :
                new_note3 = Note(data=note3, user_id=current_user.id)
        else:
            flash('Please add eather a Note or an Image to each post! (post 3)', category='error')
            return render_template('home.html', user=user, note=note, quote=quote, author=author)
        
        # Save notes
        if new_note1 != '' : db.session.add(new_note1)
        if new_note2 != '' : db.session.add(new_note2)
        if new_note3 != '' : db.session.add(new_note3)
        db.session.commit()
        flash('Note added!', category='success')
    
    return render_template('home.html', user=user, note=note, quote=quote, author=author)

@views.route("/profile")
@login_required #User can only see the profile page if they are logged in
def profile():
    ''' This view returns the profile page '''
    user = current_user
    return render_template("profile.html", user=user)

@views.route("/calendar")
@login_required
def calendar():
    return render_template("calendar.html")

@views.route("/calendar-events")
@login_required
def calendar_events():
    ''' add comment '''
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).all()
    
    note_list = []
    for notes in note:
        x = {
            "startDate": notes.date,
            "endDate": notes.date,
            "summary": notes.data,
            "image": notes.image
        }
        note_list.append(x)


    y = json.dumps(note_list, indent=4, sort_keys=True, default=str) # The result is a JSON string:

    return y

@views.route("/calendar-events-by-date/<date>")
@login_required
def calendar_events_by_date(date):
    ''' add comment '''
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).filter_by(date=date).all()
    
    note_list = []
    for notes in note:
        x = {
            "startDate": notes.date,
            "endDate": notes.date,
            "summary": notes.data,
            "image": notes.image
        }
        note_list.append(x)

    
    y = json.dumps(note_list, indent=4, sort_keys=True, default=str) # The result is a JSON string:

    return y

@views.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.password = form.password.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.password.data = current_user.password
    return render_template('edit.html', title='edit', form=form)