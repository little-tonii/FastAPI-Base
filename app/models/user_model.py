from sqlalchemy import Column, Integer, String
from app.db.database import Base

class UserModel(Base):
    __tablename__ = "users"
    id: str = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    refresh_token: str = Column(String, nullable=True)