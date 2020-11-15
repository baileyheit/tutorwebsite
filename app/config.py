import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or os.environ.get('HEROKU_POSTGRESQL_ONYX_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') 
    HEROKU_POSTGRESQL_ONYX_URL = 'postgresql-cubic-74647'
    DATABASE_URL = 'postgresql-cubic-74647'
    # postgresql-cubic-74647 as HEROKU_POSTGRESQL_ONYX_UR
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')