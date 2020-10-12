from sqlalchemy import sql, orm
from flask_sqlalchemy import SQLAlchemy
# from app import db
import app

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column('user_id', db.String(50), primary_key=True)
    user_name = db.Column('user_name', db.String(50))
    location = db.Column('location', db.String(50))
    school = db.Column('school', db.String(50))
    age = db.Column('age', db.Integer())
    phone_number = db.Column('phone_number', db.String(50))
    email = db.Column('email', db.String(50))
    address = db.Column('address', db.String(200)) #need to make this 200 in table creation
    venmo = db.Column('venmo', db.String(50))
    bio = db.Column('bio', db.String(500))

class Tutees(db.Model):
    __tablename__ = 'Tutees'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Users.user_id), primary_key=True)
    user_name = db.Column('user_name', db.String(50), db.ForeignKey(Users.user_name))
    location = db.Column('location', db.String(50), db.ForeignKey(Users.location))
    school = db.Column('school', db.String(50), db.ForeignKey(Users.school))
    age = db.Column('age', db.Integer(), db.ForeignKey(Users.age))
    phone_number = db.Column('phone_number', db.String(50), db.ForeignKey(Users.phone_number))
    email = db.Column('email', db.String(50), db.ForeignKey(Users.email))
    address = db.Column('address', db.String(200), db.ForeignKey(Users.address))
    venmo = db.Column('venmo', db.String(50), db.ForeignKey(Users.venmo))
    bio = db.Column('bio', db.String(500), db.ForeignKey(Users.bio))
    price_range = db.Column('price_range', db.String(50))
    needsHelpWith = orm.relationship('NeedsHelpWith')
    givesRating = orm.relationship('GivesRating')
    @staticmethod
    def edit(user_id, old_user_name, user_name, location, school, old_age, age, old_phone_number, phone_number, old_email, email, address, venmo, bio, price_range):
        try:
            db.session.execute('UPDATE users SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio'
                                'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
                                dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, bio=bio))
            db.session.execute('UPDATE tutees SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio, price_range = :price_range'
                                'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
                                dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, bio=bio, price_range=price_range))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Tutors(db.Model):
    __tablename__ = 'Tutors'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Users.user_id), primary_key=True)
    user_name = db.Column('user_name', db.String(50), db.ForeignKey(Users.user_name))
    location = db.Column('location', db.String(50), db.ForeignKey(Users.location))
    school = db.Column('school', db.String(50), db.ForeignKey(Users.school))
    age = db.Column('age', db.Integer(), db.ForeignKey(Users.age))
    phone_number = db.Column('phone_number', db.String(50), db.ForeignKey(Users.phone_number))
    email = db.Column('email', db.String(50), db.ForeignKey(Users.email))
    address = db.Column('address', db.String(200), db.ForeignKey(Users.address))
    venmo = db.Column('venmo', db.String(50), db.ForeignKey(Users.venmo))
    bio = db.Column('bio', db.String(500), db.ForeignKey(Users.bio))
    rating = db.Column('rating', db.Float())
    hourly_rate = db.Column('hourly_rate', db.String(50))
    grade = db.Column('grade', db.String(50))
    canTutorIn = orm.relationship('CanTutorIn')
    tutorsIn = orm.relationship('TutorsIn')    
    @staticmethod
    def edit(user_id, old_user_name, user_name, location, school, old_age, age, old_phone_number, phone_number, old_email, email, address, venmo, bio, hourly_rate, grade):
        try:
            db.session.execute('UPDATE users SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio'
                                'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
                                dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, bio=bio))
            db.session.execute('UPDATE tutees SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio, hourly_rate = :hourly_rate, grade = :grade'
                                'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
                                dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, hourly_rate=hourly_rate, grade=grade))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Classes(db.Model):
    __tablename__ = 'Classes'
    class_id = db.Column('class_id', db.String(50), primary_key=True)
    subject_name = db.Column('subject_name', db.String(50))
    class_name = db.Column('class_name', db.String(50))

class Session(db.Model):
    __tablename__ = 'Session'
    session_id = db.Column('session_id', db.Integer(), primary_key=True)
    zoom_link = db.Column('zoom_link', db.String(50))
    session_day = db.Column('session_day', db.String(50))
    price = db.Column('price', db.Float())
    booked = db.Column('booked', db.String(100))

class Cart(db.Model):
    __tablename__ = 'Cart'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Tutees.user_id), primary_key=True)
    user_name = db.Column('user_name', db.String(50), db.ForeignKey(Tutees.user_name))
    location = db.Column('location', db.String(50), db.ForeignKey(Tutees.location))
    school = db.Column('school', db.String(50), db.ForeignKey(Tutees.school))
    age = db.Column('age', db.Integer(), db.ForeignKey(Tutees.age))
    phone_number = db.Column('phone_number', db.String(50), db.ForeignKey(Tutees.phone_number))
    email = db.Column('email', db.String(50), db.ForeignKey(Tutees.email))
    address = db.Column('address', db.String(200), db.ForeignKey(Tutees.address))
    venmo = db.Column('venmo', db.String(50), db.ForeignKey(Tutees.venmo))
    bio = db.Column('bio', db.String(500), db.ForeignKey(Tutees.bio))
    price_range = db.Column('price_range', db.String(50), db.ForeignKey(Tutees.price_range))
    session_id = db.Column('session_id', db.String(50), db.ForeignKey(Session.session_id)) #add this to db?
    zoom_link = db.Column('zoom_link', db.String(50), db.ForeignKey(Session.zoom_link))
    session_day = db.Column('session_day', db.String(50), db.ForeignKey(Session.session_day))
    price = db.Column('price', db.Float(), db.ForeignKey(Session.price))
    booked = db.Column('booked', db.String(100), db.ForeignKey(Session.booked))

class CanTutorIn(db.Model):
    __tablename__ = 'CanTutorIn'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Tutors.user_id), primary_key=True)
    class_id = db.Column('class_id', db.String(50), db.ForeignKey(Classes.class_id), primary_key=True)
    # class_id = db.Column('class_id', db.String(50), db.ForeignKey(Classes.class_id)) #include this reference in db?
    expertise_lvl = db.Column('expertise_lvl', db.String(50))


class NeedsHelpWith(db.Model):
    __tablename__ = 'NeedsHelpWith'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Tutees.user_id), primary_key=True)
    class_id = db.Column('class_id', db.String(50), db.ForeignKey(Classes.class_id))

class GivesRating(db.Model):
    __tablename__ = 'GivesRating'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Tutees.user_id), primary_key = True)
    rating_comment = db.Column('rating_comment', db.String(50))
    rating_num = db.Column('rating_num', db.Float())

class TutorsIn(db.Model):
    __tablename__ = 'TutorsIn'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey(Tutors.user_id), primary_key = True)
    zoom_link = db.Column('zoom_link', db.String(50), db.ForeignKey(Session.zoom_link)) #session id instead?