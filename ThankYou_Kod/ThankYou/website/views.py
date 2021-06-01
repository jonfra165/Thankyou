from flask import Blueprint, render_template, url_for, redirect, request, flash, Flask, send_from_directory
from flask_login import login_required, current_user
from .models import Note, User
from . import db
from datetime import date
import requests
import re
import json
import os

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash #Hash for password
from validate_email import validate_email

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

def get_quote():
    '''This function gets inspirational quotes from Forismatic API'''

    response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en')
    quote_str = response.text
    quote_list = quote_str.split('(')

    quote = quote_list[0]
    if len(quote_list) == 1:
        author = 'Anonymous'
    else:
        author = quote_list[1].replace(')', '')

    return quote, author

@views.route('/', methods=['GET'])
@login_required #User can only see the home page if they are logged in
def home():
    '''This view returns the home page'''
    
    quote, author = get_quote()
    
    today = date.today()
    user = current_user.id 
    note = Note.query.filter_by(user_id=user).filter_by(date=today).all()
    note_list = []
    for notes in note:
        x = {
            "summary": notes.data if notes.data != None else "",
            "image": notes.image
        }
        note_list.append(x)

    return render_template('home.html', user=current_user, note=note_list, quote=quote, author=author)

@views.route('/send', methods=['POST'])
@login_required #User can only see the home page if they are logged in
def send_form():
    
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
            return render_template('home.html', user=current_user)

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
        
        # Save notes
        if new_note1 != '' : db.session.add(new_note1)
        if new_note2 != '' : db.session.add(new_note2)
        if new_note3 != '' : db.session.add(new_note3)
        db.session.commit()

        return redirect("/")

@views.route("/edit-note")
@login_required
def edit_note():
    '''Add comment'''

@views.route("/calendar")
@login_required
def calendar():
    return render_template("calendar.html", user=current_user)

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
            "id": notes.id,
            "startDate": notes.date,
            "endDate": notes.date,
            "summary": notes.data,
            "image": notes.image
        }
        note_list.append(x)

    
    y = json.dumps(note_list, indent=4, sort_keys=True, default=str) # The result is a JSON string:

    return y

@views.route("/delete/<id>")
@login_required
def delete(id):
    ''' Delete post from database '''

    user = current_user.id
    note = Note.query.filter_by(user_id=user).filter_by(id=id).first()

    if note:
        db.session.delete(note)
        db.session.commit()
        flash('Note successfully removed', category='success')
    else:
        flash("Note could not be removed, please try again", category='error')

    return redirect(url_for("views.calendar"))

@views.route("/profile")
@login_required #User can only see the profile page if they are logged in
def profile():
    ''' This view returns the profile page '''
    user = current_user
    return render_template("profile.html", user=user)

@views.route('/save_edit', methods=['GET', 'POST'])
@login_required
def save_edit():
    cemail = request.form.get('cemail')
    fname = request.form.get('fname')
    cpassword = request.form.get('cpassword')

    validate = validate_email(cemail)

    user = current_user.id
    profile = User.query.filter_by(id=user).first()
    
    try:
        if len(cemail) < 4:
            flash('Email must be greater than 4 characters.', category='profile-error')
        elif validate == False: 
            flash('This email does not exist', category='profile-error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 characters.', category='profile-error')
        elif cpassword == '':
            profile.email = cemail
            profile.first_name = fname
            profile.password = profile.password
            db.session.commit()
            flash('Profile updated!', category='profile-success')
        elif cpassword != '':
            if len(cpassword) < 8:
                flash('Password must be greater than 8 characters.', category='profile-error')
            elif not any(p.isupper() for p in cpassword): # Check if password includes at least one capital letter 
                flash('Password must include at least one capital letter.', category='profile-error')
            elif not any(p.isdigit() for p in cpassword): # Check if password includes at least one number 
                flash('Password must include at least one number.', category='profile-error')
            elif not any(char.islower() for char in cpassword):
                flash('Password should have at least one lowercase letter', category='profile-error')
            elif not any(char.isdigit() for char in cpassword):
                flash('Password should have at least one numeral', category='profile-error')
            else:
                profile.email = cemail
                profile.first_name = fname
                profile.password = generate_password_hash(cpassword, method='sha256')#Hash password
                db.session.commit()
                flash('Profile updated!', category='profile-success')
    except:
        flash('This account already exists in Thank You!', category='profile-error')


    return redirect(url_for('views.profile'))

@views.route("/about")
def about():

    return render_template(about.html)


