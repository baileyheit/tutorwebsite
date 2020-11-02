
from sqlalchemy import Column, Integer, String, sql, orm, VARCHAR, Float, BIGINT
from app.database import Base

class User(Base):
    __tablename__ = 'User'
    # id = Column(db.Integer, primary_key=True)
    # username = Column(db.String(64), index=True, unique=True)
    # email = Column(db.String(120), index=True, unique=True)
    # password_hash = db.Column(db.String(128))

    id = Column('id', BIGINT, primary_key=True)
    username = Column('username', String(50), primary_key=True)
    email = Column('email', String(50))
    password_hash = Column('password_hash', String(128))

    # first_name = Column('first_name', String(50))
    # last_name = Column('last_name', String(50))

    def __init__(self, username=None, password=None, email=None, first_name=None, last_name=None):
        self.username = username
        self.password = password
        self.email = email
        # self.first_name = first_name
        # self.last_name = last_name

    def __repr__(self):
        return '<User %r>' % (self.model)
