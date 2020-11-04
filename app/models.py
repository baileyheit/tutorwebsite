from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Course(db.Model):
    subject = db.Column(db.String(64), primary_key=True)
    class_num = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Course {}>'.format(self.subject)


class Session(db.Model):
    zoom_link = db.Column(db.String(120), primary_key=True)
    date = db.Column(db.DateTime, index=True)
    price = db.Column(db.Float())
    tutor = db.Column(db.Integer)
    tutee = db.Column(db.Integer)
    subject = db.Column(db.String(64))
    class_num = db.Column(db.Integer)

    def __repr__(self):
        return '<Session {}>'.format(self.zoom_link)
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    booked = db.Column(db.Boolean())


    def __repr__(self):
        return '<Post {}>'.format(self.body)  


