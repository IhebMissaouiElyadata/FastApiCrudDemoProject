from sqlalchemy.orm import Session
from ..models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, firstName:str ,lastName:str , email:str , password:str ) -> User:
        user = User(name=firstName, lastName=lastName, email=email , password=password)
        self.session.add(user)
        self.session.commit()
        return user