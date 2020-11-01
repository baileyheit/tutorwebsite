# #stores database connection information 
# from flask import Flask
# import app
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'

# db = SQLAlchemy(app)

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    
SQLALCHEMY_DATABASE_URI = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'
SQLALCHEMY_ECHO = True
DEBUG = True

