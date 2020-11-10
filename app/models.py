from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin, db.Model):
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

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Course(db.Model):
    subject = db.Column(db.String(64))
    class_num = db.Column(db.Integer)
    class_name = db.Column(db.String(200), primary_key=True)


    def __repr__(self):
        return '<Course {}>'.format(self.subject)


class Session(db.Model):
    zoom_link = db.Column(db.String(120), primary_key=True)
    date = db.Column(db.DateTime, index=True)
    time = db.Column(db.String(120))
    price = db.Column(db.Float())
    booked = db.Column(db.String(120))
    tutor = db.Column(db.Integer)
    tutee = db.Column(db.Integer)
    subject = db.Column(db.String(64))
    class_num = db.Column(db.Integer)

    def __repr__(self):
        return '<Session {}>'.format(self.zoom_link)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessions = db.Column(db.String(500))

    def __repr__(self):
        return '<Cart {}>'.format(self.body)  


