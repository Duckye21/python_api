import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, DateTime, text

from .database import Base

class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    published = Column(Boolean, server_default=text("True"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    
 # source .venv/Scripts/activate
 # uvicorn app.main:app --reload
 