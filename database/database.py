from sqlalchemy import Column,Integer,String,Boolean,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker,Session
engine = create_engine("sqlite:///codetrace.db",connect_args={"check_same_thread":False})
Base  = declarative_base()

localSession = sessionmaker(bind=engine)

# GetDB Dependency
def getDB():
    db = localSession()
    try : 
        yield db
    finally:
        db.close()
