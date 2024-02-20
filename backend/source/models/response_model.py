from sqlalchemy import Column, String, Integer, DateTime ,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Response(Base):
    __tablename__ = 'responses'

    responseId = Column(Integer, primary_key=True , autoincrement=True)
    text = Column(String )
    taskName = Column(String)
    createdAt = Column(DateTime)
    questionId = Column(Integer, ForeignKey('questions.questionId'))
    question = relationship("Question", backref="responses")