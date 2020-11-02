# import sqlalchemy
# from flask import Flask, request, redirect, url_for
# from flask import render_template
# from database import db_session
# import forms
# from models import User
# from models import Tutor
# from models import Session
# import models
# import uuid
# import pdb


# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'

# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True
# app.config['TESTING'] = True


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/tutors')
# def tutors():
#     return render_template(
#         'tutors.html',
#         tutors=Tutor.query.all()
#     )


# @app.route('/add_user')
# def add_user():
#     username = request.args.get("username")
#     password = request.args.get("password")
#     email = request.args.get("email")
#     first_name = request.args.get("first_name")
#     last_name = request.args.get("last_name")

#     user = User(username, password, email, first_name, last_name)
#     db_session.add(user)
#     db_session.commit()

#     return redirect(url_for('users'))


# @app.route('/search')
# def search():

#     price = request.args.get("price")
#     className = request.args.get("class")

#     return render_template(
#         'search.html',
#         # sessions=Session.query.join(
#         #     ForHelpIn, Session.session_id == ForHelpIn.session_id).all()
#         # sessions=Session.query.all()
#         sessions=Session.query.filter(Session.price == price)
#         # sessions=Session.query.join(
#         #     ForHelpIn, Session.session_id == ForHelpIn.session_id).filter(Session.price == price)
#     )


# if __name__ == "__main__":
#     app.run(debug=True)
