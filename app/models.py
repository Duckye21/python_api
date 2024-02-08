from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, DateTime, text
from passlib.context import CryptContext

from .database import Base


class Posts(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(Boolean, server_default=text("True"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    
    
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    
    
 # source .venv/Scripts/activate
 # uvicorn app.main:app --reload
 