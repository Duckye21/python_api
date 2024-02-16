import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData():
    id: Optional[str] = None    
    
    
class Users(BaseModel):
    email: EmailStr
    password: str
    
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime
    
    class Config:
        orm_mode = True
    
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # owner: UserResponse
    

class PostCreate(Post):
    title: str
    content: str
    published: bool = True
    
    
class Vote(BaseModel):
    user_id: int
    post_id: int
        
        