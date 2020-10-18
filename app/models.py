from sqlalchemy import Column, Integer, String, sql, orm, VARCHAR
from database import Base


class Tutor(Base):
    __tablename__ = 'Tutor'
    user_id = Column('user_id', VARCHAR(50), primary_key=True)
    user_name = Column('user_name', VARCHAR(50))
    location = Column('location', VARCHAR(50))
    school = Column('school', VARCHAR(50))
    age = Column('age', Integer())
    phone_number = Column('phone_number', VARCHAR(50))
    email = Column('email', VARCHAR(50))
    address = Column('address', VARCHAR(200))
    venmo = Column('venmo', VARCHAR(50))
    bio = Column('bio', VARCHAR(500))
    rating = Column('rating', VARCHAR(50))
    hourly_rate = Column('hourly_rate', VARCHAR(50))

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



# class Users(Base):
#     __tablename__ = 'Users'
#     user_id = Column('user_id', String(50), primary_key=True)
#     user_name = Column('user_name', String(50))
#     location = Column('location', String(50))
#     school = Column('school', String(50))
#     age = Column('age', Integer())
#     phone_number = Column('phone_number', String(50))
#     email = Column('email', String(50))
#     # need to make this 200 in table creation
#     address = Column('address', String(200))
#     venmo = Column('venmo', String(50))
#     bio = Column('bio', String(500))

#     def _init_(self, user_name=None, location=None, school=None, age=None, phone_number=None, email=None, address=None, Venmo=None, bio=None):
#         self.user_name = user_name
#         self.location = location
#         self.school = school
#         self.age = age
#         self.phone_number = phone_number
#         self.email = email
#         self.address = address
#         self.Venmo = Venmo
#         self.bio = bio

# class Tutees(Base):
#     __tablename__ = 'Tutees'
#     user_id = Column('user_id', String(50), db.ForeignKey(Users.user_id), primary_key=True)
#     user_name = Column('user_name', String(50), db.ForeignKey(Users.user_name))
#     location = Column('location', String(50), db.ForeignKey(Users.location))
#     school = Column('school', String(50), db.ForeignKey(Users.school))
#     age = Column('age', Integer(), db.ForeignKey(Users.age))
#     phone_number = Column('phone_number', String(50), db.ForeignKey(Users.phone_number))
#     email = Column('email', String(50), db.ForeignKey(Users.email))
#     address = Column('address', String(200), db.ForeignKey(Users.address))
#     venmo = Column('venmo', String(50), db.ForeignKey(Users.venmo))
#     bio = Column('bio', String(500), db.ForeignKey(Users.bio))
#     price_range = Column('price_range', String(50))
#     needsHelpWith = orm.relationship('NeedsHelpWith')
#     givesRating = orm.relationship('GivesRating')
#     @staticmethod
#     def edit(user_id, old_user_name, user_name, location, school, old_age, age, old_phone_number, phone_number, old_email, email, address, venmo, bio, price_range):
#         try:
#             db.session.execute('UPDATE users SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio'
#                                 'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
#                                 dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, bio=bio))
#             db.session.execute('UPDATE tutees SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio, price_range = :price_range'
#                                 'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
#                                 dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, bio=bio, price_range=price_range))
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e

# class Tutors(Base):
#     __tablename__ = 'Tutors'
#     user_id = Column('user_id', String(50), db.ForeignKey(Users.user_id), primary_key=True)
#     user_name = Column('user_name', String(50), db.ForeignKey(Users.user_name))
#     location = Column('location', String(50), db.ForeignKey(Users.location))
#     school = Column('school', String(50), db.ForeignKey(Users.school))
#     age = Column('age', Integer(), db.ForeignKey(Users.age))
#     phone_number = Column('phone_number', String(50), db.ForeignKey(Users.phone_number))
#     email = Column('email', String(50), db.ForeignKey(Users.email))
#     address = Column('address', String(200), db.ForeignKey(Users.address))
#     venmo = Column('venmo', String(50), db.ForeignKey(Users.venmo))
#     bio = Column('bio', String(500), db.ForeignKey(Users.bio))
#     rating = Column('rating', db.Float())
#     hourly_rate = Column('hourly_rate', String(50))
#     grade = Column('grade', String(50))
#     canTutorIn = orm.relationship('CanTutorIn')
#     tutorsIn = orm.relationship('TutorsIn')
#     @staticmethod
#     def edit(user_id, old_user_name, user_name, location, school, old_age, age, old_phone_number, phone_number, old_email, email, address, venmo, bio, hourly_rate, grade):
#         try:
#             db.session.execute('UPDATE users SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio'
#                                 'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
#                                 dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, bio=bio))
#             db.session.execute('UPDATE tutees SET user_id = :user_id, user_name = :user_name, location = :location, school = :school, age = :age, phone_number = :phone_number, email = :email, address = :address, venmo = :venmo, bio = :bio, hourly_rate = :hourly_rate, grade = :grade'
#                                 'WHERE user_name = :old_user_name OR age = :old_age OR phone_number = :old_phone_number OR email = :old_email',
#                                 dict(user_id=user_id, old_user_name=old_user_name, location=location, school=school, old_age=old_age, old_phone_number=old_phone_number, old_email=old_email, address=address, venmo=venmo, hourly_rate=hourly_rate, grade=grade))
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e

# class Classes(Base):
#     __tablename__ = 'Classes'
#     class_id = Column('class_id', String(50), primary_key=True)
#     subject_name = Column('subject_name', String(50))
#     class_name = Column('class_name', String(50))

# class Session(Base):
#     __tablename__ = 'Session'
#     session_id = Column('session_id', Integer(), primary_key=True)
#     zoom_link = Column('zoom_link', String(50))
#     session_day = Column('session_day', String(50))
#     price = Column('price', db.Float())
#     booked = Column('booked', String(100))

# class Cart(Base):
#     __tablename__ = 'Cart'
#     user_id = Column('user_id', String(50), db.ForeignKey(Tutees.user_id), primary_key=True)
#     user_name = Column('user_name', String(50), db.ForeignKey(Tutees.user_name))
#     location = Column('location', String(50), db.ForeignKey(Tutees.location))
#     school = Column('school', String(50), db.ForeignKey(Tutees.school))
#     age = Column('age', Integer(), db.ForeignKey(Tutees.age))
#     phone_number = Column('phone_number', String(50), db.ForeignKey(Tutees.phone_number))
#     email = Column('email', String(50), db.ForeignKey(Tutees.email))
#     address = Column('address', String(200), db.ForeignKey(Tutees.address))
#     venmo = Column('venmo', String(50), db.ForeignKey(Tutees.venmo))
#     bio = Column('bio', String(500), db.ForeignKey(Tutees.bio))
#     price_range = Column('price_range', String(50), db.ForeignKey(Tutees.price_range))
#     session_id = Column('session_id', String(50), db.ForeignKey(Session.session_id)) #add this to db?
#     zoom_link = Column('zoom_link', String(50), db.ForeignKey(Session.zoom_link))
#     session_day = Column('session_day', String(50), db.ForeignKey(Session.session_day))
#     price = Column('price', db.Float(), db.ForeignKey(Session.price))
#     booked = Column('booked', String(100), db.ForeignKey(Session.booked))

# class CanTutorIn(Base):
#     __tablename__ = 'CanTutorIn'
#     user_id = Column('user_id', String(50), db.ForeignKey(Tutors.user_id), primary_key=True)
#     class_id = Column('class_id', String(50), db.ForeignKey(Classes.class_id), primary_key=True)
#     # class_id = Column('class_id', String(50), db.ForeignKey(Classes.class_id)) #include this reference in db?
#     expertise_lvl = Column('expertise_lvl', String(50))


# class NeedsHelpWith(Base):
#     __tablename__ = 'NeedsHelpWith'
#     user_id = Column('user_id', String(50), db.ForeignKey(Tutees.user_id), primary_key=True)
#     class_id = Column('class_id', String(50), db.ForeignKey(Classes.class_id))

# class GivesRating(Base):
#     __tablename__ = 'GivesRating'
#     user_id = Column('user_id', String(50), db.ForeignKey(Tutees.user_id), primary_key = True)
#     rating_comment = Column('rating_comment', String(50))
#     rating_num = Column('rating_num', db.Float())

# class TutorsIn(Base):
#     __tablename__ = 'TutorsIn'
#     user_id = Column('user_id', String(50), db.ForeignKey(Tutors.user_id), primary_key = True)
#     zoom_link = Column('zoom_link', String(50), db.ForeignKey(Session.zoom_link)) #session id instead?
