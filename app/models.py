<<<<<<< HEAD
<<<<<<< HEAD
# from sqlalchemy import Column, Integer, String, sql, orm, VARCHAR, Float, BIGINT
# from .database import Base
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
# from .app import login
=======
from app import db
>>>>>>> d52ce842755054e4c58dc362170161c9402f0844

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

<<<<<<< HEAD
# class User(UserMixin, Base):
#     __tablename__ = 'User'
#     phone_number = Column('phone_number', BIGINT())
#     address = Column('address', String(200))
#     user_name = Column('user_name', String(50))
#     user_id = Column('user_id', String(50), primary_key=True)
#     user_password = Column('password', String(50), primary_key=True)
#     location = Column('location', String(50))
#     school = Column('school', String(50))
#     age = Column('age', Integer())
#     email = Column('email', String(50))
#     venmo = Column('venmo', String(50))
#     bio = Column('bio', String(500))

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     # def __init__(self, phone_number=None, user_password=None, address=None, user_name=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None):
#     def __init__(self, phone_number=None, user_password=None, address=None, user_name=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None):
#         self.phone_number = phone_number
#         self.address = address
#         self.user_name = user_name
#         self.user_id = user_id
#         self.user_password = user_password
#         self.location = location
#         self.school = school
#         self.age = age
#         self.email = email
#         self.venmo = venmo
#         self.bio = bio

#     def __repr__(self):
#         return '<User %r>' % (self.model)

# @login.user_loader
# def load_user(user_id):
#     return User.query.get(int(id))

# class Tutor(Base):
#     __tablename__ = 'Tutor'
#     phone_number = Column('phone_number', BIGINT())
#     address = Column('address', String(200))
#     user_name = Column('user_name', String(50)) #this is the users FULL NAME 
#     user_password = Column('password', String(50)) 
#     user_id = Column('user_id', String(50), primary_key=True) #this is the user's UNIQUE USERNAME
#     location = Column('location', String(50))
#     school = Column('school', String(50))
#     age = Column('age', Integer())
#     email = Column('email', String(50))
#     venmo = Column('venmo', String(50))
#     bio = Column('bio', String(500))
#     rating = Column('rating', Float())
#     hourly_rate = Column('hourly_rate', Float())
#     grade = Column('grade', String(50))

#     def __init__(self, phone_number=None, address=None, user_name=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None, rating=None, hourly_rate=None, grade=None):
#         self.phone_number = phone_number
#         self.address = address
#         self.user_name = user_name
#         self.user_id = user_id
#         self.location = location
#         self.school = school
#         self.age = age
#         self.email = email
#         self.venmo = venmo
#         self.bio = bio
#         self.rating = rating
#         self.hourly_rate = hourly_rate
#         self.grade = grade

#     def __repr__(self):
#         return '<Tutor %r>' % (self.model)


# class Tuttee(Base):
#     __tablename__ = 'Tuttee'
#     phone_number = Column('phone_number', BIGINT())
#     address = Column('address', String(200))
#     user_name = Column('user_name', String(50))
#     password = Column('password', String(50))
#     user_id = Column('user_id', String(50), primary_key=True)
#     location = Column('location', String(50))
#     school = Column('school', String(50))
#     age = Column('age', Integer())
#     email = Column('email', String(50))
#     venmo = Column('venmo', String(50))
#     bio = Column('bio', String(500))
#     price_range = Column('price_range', String(50))

#     def __init__(self, phone_number=None, address=None, user_name=None, password=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None, price_range=None):
#         self.phone_number = phone_number
#         self.address = address
#         self.user_name = user_name
#         self.password = password
#         self.user_id = user_id
#         self.location = location
#         self.school = school
#         self.age = age
#         self.email = email
#         self.venmo = venmo
#         self.bio = bio
#         self.price_range = price_range

#     def __repr__(self):
#         return '<Tuttee %r>' % (self.model)


# class CanTutorIn(Base):
#     __tablename__ = 'CanTutorIn'
#     user_id = Column('user_id', BIGINT(), primary_key=True)
#     class_id = Column('class_id', String(200))
#     expertise_lvl = Column('expertise_lvl', String(200))

#     def _init_(self, user_id=None, class_id=None, expertise_lvl=None):
#         self.user_id = user_id
#         self.class_id = class_id
#         self.expertise_lvl = expertise_lvl

#     def __repr__(self):
#         return '<CanTutorIn %r>' % (self.model)


# class TutorsIn(Base):
#     __tablename__ = 'TutorsIn'
#     session_id = Column('session_id', BIGINT(), primary_key=True)
#     class_id = Column('class_id', String(200))

#     def _init_(self, session_id=None, class_id=None):
#         self.session_id = session_id
#         self.class_id = class_id

#     def __repr__(self):
#         return '<TutorsIn %r>' % (self.model)


# class Cart(Base):
#     __tablename__ = 'Cart'
#     user_id = Column('user_id', BIGINT(), primary_key=True)
#     session_id = Column('session_id', String(200))

#     def _init_(self, user_id=None, session_id=None):
#         self.user_id = user_id
#         self.session_id = session_id

#     def __repr__(self):
#         return '<Cart %r>' % (self.model)


# class ForHelpIn(Base):
#     __tablename__ = 'ForHelpIn'
#     session_id = Column('session_id', BIGINT(), primary_key=True)
#     class_id = Column('class_id', String(500))

#     def _init_(self, session_id=None, class_id=None):
#         self.session_id = session_id
#         self.class_id = class_id

#     def __repr__(self):
#         return '<ForHelpIn %r>' % (self.model)


# class GetsHelpIn(Base):
#     __tablename__ = 'GetsHelpIn'
#     session_id = Column('session_id', BIGINT(), primary_key=True)
#     class_id = Column('class_id', String(500))

#     def _init_(self, session_id=None, class_id=None):
#         self.session_id = session_id
#         self.class_id = class_id

#     def __repr__(self):
#         return '<GetsHelpIn %r>' % (self.model)


# # class GivesRating(Base):
# #     __tablename__ = 'GivesRating'
# #     tutor_id = Column('tutor_id', BIGINT())
# #     tuttee_id = Column('tuttee_id', BIGINT())
# #     rating_comment = Column('rating_comment', String(500))
# #     rating_num = Column('rating_num', Integer())

# #     def _init_(self, tutor_id=None, tuttee_id=None, rating_comment=None, rating_num=None):
# #         self.tutor_id = tutor_id
# #         self.tuttee_id = tuttee_id
# #         self.rating_comment = rating_comment
# #         self.rating_num = rating_num

# #     def __repr__(self):
# #         return '<GivesRating %r>' % (self.model)


# class NeedsHelpWith(Base):
#     __tablename__ = 'NeedsHelpWith'
#     user_id = Column('user_id', BIGINT(), primary_key=True)
#     class_id = Column('class_id', String(500))

#     def _init_(self, user_id=None, class_id=None):
#         self.user_id = user_id
#         self.class_id = class_id

#     def __repr__(self):
#         return '<NeedsHelpWith %r>' % (self.model)


# class Session(Base):
#     __tablename__ = 'Session'
#     session_id = Column('session_id', BIGINT(), primary_key=True)
#     zoom_link = Column('zoom_link', String(100))
#     session_day = Column('session_day', String(50))
#     session_time = Column('session_time', String(50))
#     price = Column('price', String(20))
#     booked = Column('booked', String(100))
#     tutorsin = Column('tutorsin', String(50))
#     gets_help_in = Column('gets_help_in', BIGINT())

#     def _init_(self, session_id=None, zoom_link=None, session_day=None, session_time=None, price=None, booked=None, tutorsin=None, gets_help_in=None):
#         self.session_id = session_id
#         self.zoom_link = zoom_link
#         self.session_day = session_day
#         self.session_time = session_time
#         self.price = price
#         self.booked = booked
#         self.tutorsin = tutorsin
#         self.gets_help_in = gets_help_in

#     def __repr__(self):
#         return '<Session %r>' % (self.model)
=======
from sqlalchemy import Column, Integer, String, sql, orm, VARCHAR, Float, BIGINT
from database import Base


class User(Base):
    __tablename__ = 'User'
    user_name = Column('username', String(50), primary_key=True)
    password = Column('password', String(50))
    email = Column('email', String(50))
    first_name = Column('first_name', String(50))
    last_name = Column('last_name', String(50))

    def __init__(self, username=None, password=None, email=None, first_name=None, last_name=None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %r>' % (self.model)


class Tutor(Base):
    __tablename__ = 'Tutor'
    username = Column('username', String(50), primary_key=True)
    phone_number = Column('phone_number', BIGINT())
    address = Column('address', String(200))
    location = Column('location', String(50))
    school = Column('school', String(50))
    age = Column('age', Integer())
    venmo = Column('venmo', String(50))
    bio = Column('bio', String(500))
    rating = Column('rating', Float())
    hourly_rate = Column('hourly_rate', Float())
    grade = Column('grade', String(50))

    def __init__(self, username=None, phone_number=None, address=None, location=None, school=None, age=None, venmo=None, bio=None, rating=None, hourly_rate=None, grade=None):
        self.username = username
        self.phone_number = phone_number
        self.address = address
        self.location = location
        self.school = school
        self.age = age
        self.venmo = venmo
        self.bio = bio
        self.rating = rating
        self.hourly_rate = hourly_rate
        self.grade = grade

    def __repr__(self):
        return '<Tutor %r>' % (self.model)


class Tuttee(Base):
    __tablename__ = 'Tuttee'
    username = Column('username', String(50), primary_key=True)
    phone_number = Column('phone_number', BIGINT())
    address = Column('address', String(200))
    location = Column('location', String(50))
    school = Column('school', String(50))
    age = Column('age', Integer())
    venmo = Column('venmo', String(50))
    bio = Column('bio', String(500))
    price_range = Column('price_range', String(50))

    def __init__(self, username=None, phone_number=None, address=None, location=None, school=None, age=None, venmo=None, bio=None, price_range=None):
        self.username = username
        self.phone_number = phone_number
        self.address = address
        self.location = location
        self.school = school
        self.age = age
        self.venmo = venmo
        self.bio = bio
        self.price_range = price_range

    def __repr__(self):
        return '<Tuttee %r>' % (self.model)


class CanTutorIn(Base):
    __tablename__ = 'CanTutorIn'
    username = Column('username', String(50), primary_key=True)
    class_id = Column('class_id', String(200))
    expertise_lvl = Column('expertise_lvl', String(200))

    def _init_(self, username=None, class_id=None, expertise_lvl=None):
        self.username = username
        self.class_id = class_id
        self.expertise_lvl = expertise_lvl

    def __repr__(self):
        return '<CanTutorIn %r>' % (self.model)


class Cart(Base):
    __tablename__ = 'Cart'
    username = Column('username', String(50), primary_key=True)
    session_id = Column('session_id', String(200))

    def _init_(self, username=None, session_id=None):
        self.username = username
        self.session_id = session_id

    def __repr__(self):
        return '<Cart %r>' % (self.model)


class GivesRating(Base):
    __tablename__ = 'GivesRating'
    rating_id = Column('rating_id', BIGINT(), primary_key=True)
    tutor = Column('tutor', String(50))
    tutee = Column('tutee', String(50))
    session = Column('session', String(50))
    subject = Column('subject', String(50))
    rating_comment = Column('rating_comment', String(500))
    rating_num = Column('rating_num', Integer())

    def _init_(self, rating_id=None, tutor=None, tutee=None, session=None, subject=None, rating_comment=None, rating_num=None):
        self.rating_id = rating_id
        self.tutor = tutor
        self.tutee = tutee
        self.session = session
        self.subject = subject 
        self.rating_comment = rating_comment
        self.rating_num = rating_num

    def __repr__(self):
        return '<GivesRating %r>' % (self.model)


class NeedsHelpWith(Base):
    __tablename__ = 'NeedsHelpWith'
    username = Column('username', String(50), primary_key=True)
    class_id = Column('class_id', String(50))

    def _init_(self, username=None, class_id=None):
        self.username = username
        self.class_id = class_id

    def __repr__(self):
        return '<NeedsHelpWith %r>' % (self.model)


class Session(Base):
    __tablename__ = 'Session'
    session_id = Column('session_id', BIGINT(), primary_key=True)
    zoom_link = Column('zoom_link', String(100))
    session_day = Column('session_day', String(50))
    session_time = Column('session_time', String(50))
    price = Column('price', Float())
    booked = Column('booked', String(100))
    tutor = Column('tutor', String(50))
    tutee = Column('tutee', String(50))
    subject = Column('subject', String(50))

    def _init_(self, session_id=None, zoom_link=None, session_day=None, session_time=None, price=None, booked=None, tutor=None, tutee=None, subject=None):
        self.session_id = session_id
        self.zoom_link = zoom_link
        self.session_day = session_day
        self.session_time = session_time
        self.price = price
        self.booked = booked
        self.tutor = tutor
        self.tutee = tutee 
        self.subject = subject

    def __repr__(self):
        return '<Session %r>' % (self.model)
>>>>>>> 29ac1d8b9ae95a0ea43482984c0e077a4cc9ffb7
=======
    def __repr__(self):
        return '<User {}>'.format(self.username)  
<<<<<<< HEAD
>>>>>>> d52ce842755054e4c58dc362170161c9402f0844
=======
        
>>>>>>> 35dba9c163cef20d55eb38aa761005efcb338059
