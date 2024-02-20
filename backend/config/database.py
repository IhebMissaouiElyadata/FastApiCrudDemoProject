from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Appconfig

config = Appconfig()
#Data base url from envir variable
DataBaseURL = config.database_url

#Create an engine to connect to the PostegreSQL database
engine = create_engine(DataBaseURL, echo=True)

#Create a sessionMaker to create sessions
Session = sessionmaker(bind=engine)

def get_session():
    """"Function to get a database session"""
    return Session()