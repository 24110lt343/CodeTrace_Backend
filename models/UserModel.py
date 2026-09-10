from database.database import Base 
from sqlalchemy import Column,Integer,String,Boolean

class UserModel(Base):
    __tablename__ = "UserTable"
    id = Column(Integer,autoincrement=True,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
