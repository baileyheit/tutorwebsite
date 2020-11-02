from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config.from_object(Config)
# db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
