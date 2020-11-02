import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG = True
    SERVER_NAME=127.0.0.1:5001
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'
#     # SQLALCHEMY_DATABASE_URI = 'mysql://newuser:pass@localhost/tutorwebsite'
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#     #     'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_ECHO = True
#     DEBUG = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
