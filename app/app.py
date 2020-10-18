import sqlalchemy
from flask import Flask, request, redirect, url_for
from flask import render_template
from database import db_session
# import models
import forms
# from models import Users
from models import Tutor
import uuid
import pdb


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'

# @app.route('/')
# def hello_world():
#   return 'Hello, World!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

id = uuid.uuid1()


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/users')
# def users():
#     return render_template(
#         'all_tutors.html',
#         users=Users.query.all()
#     )


@app.route('/tutors')
def tutors():
    return render_template(
        'tutors.html',
        tutors=Tutor.query.all()
    )


@app.route('/add_tutor')
def add_tutor():
    user_id = id.int
    user_name = request.args.get("name")
    location = request.args.get("location")
    school = request.args.get("school")
    age = request.args.get("age")
    phone_number = request.args.get("phone number")
    email = request.args.get("email")
    address = request.args.get("address")
    venmo = request.args.get("venmo")
    bio = request.args.get("bio")
    rating = 0.0
    hourly_rate = request.args.get("hourly rate")
    grade = request.args.get("grade")

    # tutor = Tutor(user_id, user_name, location, school, age, phone_number,
    #               email, address, venmo, bio, rating, hourly_rate, grade)

    tutor = Tutor(phone_number, address, user_name, user_id, location,
                  school, age, email, venmo, bio, rating, hourly_rate, grade)
    db_session.add(tutor)
    db_session.commit()

    return redirect(url_for('tutors'))

    #     user_id = Column('user_id', VARCHAR(50), primary_key=True)
    # user_name = Column('user_name', VARCHAR(50))
    # location = Column('location', VARCHAR(50))
    # school = Column('school', VARCHAR(50))
    # age = Column('age', Integer())
    # phone_number = Column('phone_number', VARCHAR(50))
    # email = Column('email', VARCHAR(50))
    # address = Column('address', VARCHAR(200))
    # venmo = Column('venmo', VARCHAR(50))
    # bio = Column('bio', VARCHAR(500))
    # rating = Column('rating', VARCHAR(50))
    # hourly_rate = Column('hourly_rate', VARCHAR(50))

# def all_tutors():
#   tutors = db.session.query(models.Tutors).all()
#   return render_template('all-tutors.html', tutors=tutors)                        #implement all-tutors.html template

# @app.route('/tutors', methods=['GET', 'POST'])
# def tutors():
#   class_names = [c.class_id for c in db.session.query(models.CanTutorIn).all()]
#   form = forms.TutorsFormFactory.form(class_names=class_names)                    #implement TutorsFormFactory function in forms.py
#   if form.validate_on_submit():
#     return redirect('/tutors/'+form.class_sel.data)
#   return render_template('tutors.html', form=form)                                #implement tutors.html template

# @app.route('/tutors/<class_name>')
# def tutors_in(class_name):
#   results = db.session.query(models.CanTutorIn, models.Users) \
#                       .filter(models.CanTutorIn.class_id == class_name) \
#                       .join(models.Users).all()
#   return render_template('tutors_in.html', class_name=class_name, data=results)   #implement tutors_in.html template


# # @app.route('/')
# # def hello_world():
# #     return 'Hello, World!'

# # mysql://username:password@server/db

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
if __name__ == "__main__":
    app.run(debug=True)
