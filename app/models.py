from sqlalchemy import UniqueConstraint
from datetime import datetime, date, time
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time
import jwt
from app import app

class usertable(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(128))
    phone_number = db.Column(db.Integer)
    school = db.Column(db.String(128))
    venmo = db.Column(db.String(128))
    about_me = db.Column(db.String(500))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    rating = db.Column(db.Float())
    hourly_rate = db.Column(db.Float())
    grade = db.Column(db.String(128))
    price_range = db.Column(db.Float())

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return usertable.query.get(id)

@login.user_loader
def load_user(id):
    return usertable.query.get(int(id))


class coursetable(db.Model):
    subject = db.Column(db.String(64))
    class_num = db.Column(db.Integer)
    class_name = db.Column(db.String(200), primary_key=True)

    def __repr__(self):
        return '<Course {}>'.format(self.class_name)


class sessiontable(db.Model):
    session_id = db.Column(db.Integer, primary_key=True)
    zoom_link = db.Column(db.String(120))
    date = db.Column(db.String(120))
    time = db.Column(db.String(120))
    price = db.Column(db.Float())
    booked = db.Column(db.String(120))
    tutor = db.Column(db.Integer, db.ForeignKey('usertable.id'))
    tutee = db.Column(db.Integer, db.ForeignKey('usertable.id'))
    subject = db.Column(db.String(120))
    class_num = db.Column(db.Integer)

    def __repr__(self):
        return '<Session {}>'.format(self.zoom_link)

class carttable(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer)
    id = db.Column(db.Integer, db.ForeignKey('usertable.id'))

    def __repr__(self):
        return '<Cart {}>'.format(self.id)

class ratingtable(db.Model):
    rating_id = db.Column(db.Integer, primary_key=True)
    tutor = db.Column(db.Integer, db.ForeignKey('usertable.id'))
    tutee = db.Column(db.Integer, db.ForeignKey('usertable.id'))
    session = db.Column(db.Integer, db.ForeignKey('sessiontable.session_id'))
    subject = db.Column(db.String(64))
    class_num = db.Column(db.Integer)
    comment = db.Column(db.String(500))
    rating_num = db.Column(db.Integer)

    def __repr__(self):
        return '<Rating {}>'.format(self.rating_id)
