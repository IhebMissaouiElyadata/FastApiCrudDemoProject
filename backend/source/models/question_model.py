from sqlalchemy import Column, String, Integer, DateTime ,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    questionId = Column(Integer, primary_key=True , autoincrement=True)
    text = Column(String )
    taskName = Column(String)
    createdAt = Column(DateTime)
    discussionId = Column(Integer, ForeignKey('discussions.discussionId'))
    discussion = relationship("Discussion", backref="questions")