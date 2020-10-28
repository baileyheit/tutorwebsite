from sqlalchemy import Column, Integer, String, sql, orm, VARCHAR, Float, BIGINT
from database import Base


class User(Base):
    __tablename__ = 'User'
    phone_number = Column('phone_number', BIGINT())
    address = Column('address', String(200))
    user_name = Column('user_name', String(50))
    user_id = Column('user_id', String(50), primary_key=True)
    location = Column('location', String(50))
    school = Column('school', String(50))
    age = Column('age', Integer())
    email = Column('email', String(50))
    venmo = Column('venmo', String(50))
    bio = Column('bio', String(500))

    def __init__(self, phone_number=None, address=None, user_name=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None):
        self.phone_number = phone_number
        self.address = address
        self.user_name = user_name
        self.user_id = user_id
        self.location = location
        self.school = school
        self.age = age
        self.email = email
        self.venmo = venmo
        self.bio = bio

    def __repr__(self):
        return '<User %r>' % (self.model)


class Tutor(Base):
    __tablename__ = 'Tutor'
    phone_number = Column('phone_number', BIGINT())
    address = Column('address', String(200))
    user_name = Column('user_name', String(50))
    user_password = Column('password', String(50))
    user_id = Column('user_id', String(50), primary_key=True)
    location = Column('location', String(50))
    school = Column('school', String(50))
    age = Column('age', Integer())
    email = Column('email', String(50))
    venmo = Column('venmo', String(50))
    bio = Column('bio', String(500))
    rating = Column('rating', Float())
    hourly_rate = Column('hourly_rate', Float())
    grade = Column('grade', String(50))

    def __init__(self, phone_number=None, address=None, user_name=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None, rating=None, hourly_rate=None, grade=None):
        self.phone_number = phone_number
        self.address = address
        self.user_name = user_name
        self.user_id = user_id
        self.location = location
        self.school = school
        self.age = age
        self.email = email
        self.venmo = venmo
        self.bio = bio
        self.rating = rating
        self.hourly_rate = hourly_rate
        self.grade = grade

    def __repr__(self):
        return '<Tutor %r>' % (self.model)


class Tuttee(Base):
    __tablename__ = 'Tuttee'
    phone_number = Column('phone_number', BIGINT())
    address = Column('address', String(200))
    user_name = Column('user_name', String(50))
    password = Column('password', String(50))
    user_id = Column('user_id', String(50), primary_key=True)
    location = Column('location', String(50))
    school = Column('school', String(50))
    age = Column('age', Integer())
    email = Column('email', String(50))
    venmo = Column('venmo', String(50))
    bio = Column('bio', String(500))
    price_range = Column('price_range', String(50))

    def __init__(self, phone_number=None, address=None, user_name=None, password=None, user_id=None, location=None, school=None, age=None, email=None, venmo=None, bio=None, price_range=None):
        self.phone_number = phone_number
        self.address = address
        self.user_name = user_name
        self.password = password
        self.user_id = user_id
        self.location = location
        self.school = school
        self.age = age
        self.email = email
        self.venmo = venmo
        self.bio = bio
        self.price_range = price_range

    def __repr__(self):
        return '<Tuttee %r>' % (self.model)


class CanTutorIn(Base):
    __tablename__ = 'CanTutorIn'
    user_id = Column('user_id', BIGINT(), primary_key=True)
    class_id = Column('class_id', String(200))
    expertise_lvl = Column('expertise_lvl', String(200))

    def _init_(self, user_id=None, class_id=None, expertise_lvl=None):
        self.user_id = user_id
        self.class_id = class_id
        self.expertise_lvl = expertise_lvl

    def __repr__(self):
        return '<CanTutorIn %r>' % (self.model)


class TutorsIn(Base):
    __tablename__ = 'TutorsIn'
    session_id = Column('session_id', BIGINT(), primary_key=True)
    class_id = Column('class_id', String(200))

    def _init_(self, session_id=None, class_id=None):
        self.session_id = session_id
        self.class_id = class_id

    def __repr__(self):
        return '<TutorsIn %r>' % (self.model)


class Cart(Base):
    __tablename__ = 'Cart'
    user_id = Column('user_id', BIGINT(), primary_key=True)
    session_id = Column('session_id', String(200))

    def _init_(self, user_id=None, session_id=None):
        self.user_id = user_id
        self.session_id = session_id

    def __repr__(self):
        return '<Cart %r>' % (self.model)


class ForHelpIn(Base):
    __tablename__ = 'ForHelpIn'
    session_id = Column('session_id', BIGINT(), primary_key=True)
    class_id = Column('class_id', String(500))

    def _init_(self, session_id=None, class_id=None):
        self.session_id = session_id
        self.class_id = class_id

    def __repr__(self):
        return '<ForHelpIn %r>' % (self.model)


class GetsHelpIn(Base):
    __tablename__ = 'GetsHelpIn'
    session_id = Column('session_id', BIGINT(), primary_key=True)
    class_id = Column('class_id', String(500))

    def _init_(self, session_id=None, class_id=None):
        self.session_id = session_id
        self.class_id = class_id

    def __repr__(self):
        return '<GetsHelpIn %r>' % (self.model)


# class GivesRating(Base):
#     __tablename__ = 'GivesRating'
#     tutor_id = Column('tutor_id', BIGINT())
#     tuttee_id = Column('tuttee_id', BIGINT())
#     rating_comment = Column('rating_comment', String(500))
#     rating_num = Column('rating_num', Integer())

#     def _init_(self, tutor_id=None, tuttee_id=None, rating_comment=None, rating_num=None):
#         self.tutor_id = tutor_id
#         self.tuttee_id = tuttee_id
#         self.rating_comment = rating_comment
#         self.rating_num = rating_num

#     def __repr__(self):
#         return '<GivesRating %r>' % (self.model)


class NeedsHelpWith(Base):
    __tablename__ = 'NeedsHelpWith'
    user_id = Column('user_id', BIGINT(), primary_key=True)
    class_id = Column('class_id', String(500))

    def _init_(self, user_id=None, class_id=None):
        self.user_id = user_id
        self.class_id = class_id

    def __repr__(self):
        return '<NeedsHelpWith %r>' % (self.model)


class Session(Base):
    __tablename__ = 'Session'
    session_id = Column('session_id', BIGINT(), primary_key=True)
    zoom_link = Column('zoom_link', String(100))
    session_day = Column('session_day', String(50))
    session_time = Column('session_time', String(50))
    price = Column('price', String(20))
    booked = Column('booked', String(100))
    tutorsin = Column('tutorsin', String(50))
    gets_help_in = Column('gets_help_in', BIGINT())

    def _init_(self, session_id=None, zoom_link=None, session_day=None, session_time=None, price=None, booked=None, tutorsin=None, gets_help_in=None):
        self.session_id = session_id
        self.zoom_link = zoom_link
        self.session_day = session_day
        self.session_time = session_time
        self.price = price
        self.booked = booked
        self.tutorsin = tutorsin
        self.gets_help_in = gets_help_in

    def __repr__(self):
        return '<Session %r>' % (self.model)
