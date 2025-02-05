from pydantic import BaseModel, EmailStr, Field


class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field()