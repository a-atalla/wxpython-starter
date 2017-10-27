from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationships, backref
from passlib.hash import pbkdf2_sha256
from . import Base


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    password = Column(String(150))

    def __init__(self, username, password, first_name='', last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = pbkdf2_sha256.hash(password)

    def __repr__(self):
        return '<User "{} {}">'.format(self.first_name, self.last_name)
