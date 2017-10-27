from .prepare import Base, Session
from .user import User

def create_db():
    Base.metadata.create_all()
