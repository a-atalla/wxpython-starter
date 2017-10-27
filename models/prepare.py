from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///demo.db')
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
