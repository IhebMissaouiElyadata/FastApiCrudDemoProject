from sqlalchemy import Column, Integer, String , ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from  sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True , autoincrement=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
