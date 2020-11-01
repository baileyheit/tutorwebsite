import sqlalchemy
from flask import Flask, request, redirect, url_for
from flask import render_template
from database import db_session
import forms
from models import Tutor
from models import Session
import models
import uuid
import pdb


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tutors')
def tutors():
    return render_template(
        'tutors.html',
        tutors=Tutor.query.all()
    )


@app.route('/add_tutor')
def add_tutor():
    user_id = uuid.uuid4().int
    user_name = request.args.get("name")
    user_name = request.args.get("password")
    location = request.args.get("location")
    school = request.args.get("school")
    age = request.args.get("age")
    phone_number = request.args.get("phone_number")
    email = request.args.get("email")
    address = request.args.get("address")
    venmo = request.args.get("venmo")
    bio = request.args.get("bio")
    rating = 0.0
    hourly_rate = request.args.get("hourly_rate")
    grade = request.args.get("grade")

    tutor = Tutor(phone_number, address, user_name, password, user_id, location,
                  school, age, email, venmo, bio, rating, hourly_rate, grade)
    db_session.add(tutor)
    db_session.commit()

    return redirect(url_for('tutors'))


@app.route('/search')
def search():

    price = request.args.get("price")
    className = request.args.get("class")

    return render_template(
        'search.html',
        # sessions=Session.query.join(
        #     ForHelpIn, Session.session_id == ForHelpIn.session_id).all()
        # sessions=Session.query.all()
        sessions=Session.query.filter(Session.price == price)
        # sessions=Session.query.join(
        #     ForHelpIn, Session.session_id == ForHelpIn.session_id).filter(Session.price == price)
    )


if __name__ == "__main__":
    app.run(debug=True)
