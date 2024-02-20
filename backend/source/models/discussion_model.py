from sqlalchemy import Column, String, Integer, DateTime ,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Discussion(Base):
    __tablename__ = 'discussion'

    questionId = Column(Integer, primary_key=True , autoincrement=True)
    text = Column(String )
    taskName = Column(String)
    createdAt = Column(DateTime)
    userId = Column(Integer, ForeignKey('users.userId'))
    user = relationship("User", backref="discussions")