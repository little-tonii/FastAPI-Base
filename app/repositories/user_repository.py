from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_database
from app.models.user_model import UserModel

class UserRepository:
    __database: Session
    
    def __init__(self, database: Annotated[Session, Depends(get_database)]):
        self.__database = database
        
    def create_user(self, email: str, hased_password: str):
        user_model = UserModel(email=email, hashed_password=hased_password)
        self.__database.add(user_model)
        self.__database.commit()
        
    def find_user_by_email(self, email: str) -> UserModel | None:
        return self.__database.query(UserModel).filter(UserModel.email == email).first()
    
    def find_user_by_id(self, id: int) -> UserModel | None:
        return self.__database.query(UserModel).filter(UserModel.id == id).first()
    
    def update_user(self, user: UserModel):
        self.__database.add(user)
        self.__database.commit()
        