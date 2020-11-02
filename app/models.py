
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
