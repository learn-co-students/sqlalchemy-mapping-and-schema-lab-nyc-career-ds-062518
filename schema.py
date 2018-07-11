import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Musician(Base):
    __tablename__ = "musicians"
    id = Column(Integer, primary_key = True)
    fullname = Column(VARCHAR)
    instrument = Column(VARCHAR)
    dob = Column(DATETIME)
    alive = Column(BOOLEAN)

engine = create_engine('sqlite:///musicians.db', echo=True)
Base.metadata.create_all(engine)
