import datetime
from pydantic import BaseModel, EmailStr
# from typing import Optional


class Posts(BaseModel):
    # id: Optional[int] = None
    title: str
    content: str
    published: bool = True
    
    
class Users(BaseModel):
    email: EmailStr
    password: str
    
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime
    
    class Config:
        orm_mode = True
    
        