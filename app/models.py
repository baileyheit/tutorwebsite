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
